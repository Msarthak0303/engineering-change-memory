import json
import os
from uuid import uuid4

from openai import AsyncOpenAI


class ChangeAgent:
    def __init__(self, memory):
        self.memory = memory
        self.llm = AsyncOpenAI(
            api_key=os.getenv("LLM_API_KEY", ""),
            base_url=os.getenv(
                "LLM_BASE_URL",
                "https://api.groq.com/openai/v1",
            ),
        )
        self.model = os.getenv(
            "LLM_MODEL",
            "openai/gpt-oss-120b",
        )

    async def analyze(self, change: dict):
        change_id = str(uuid4())

        recall_query = (
            "Find previous engineering changes similar to this upcoming change. "
            "Focus on the same service, change type, failure modes, mitigations, "
            "outcomes, and lessons learned. Upcoming change: "
            + json.dumps(change)
        )

        recalled = await self.memory.recall(recall_query)

        # Extract only the useful Hindsight memory fields.
        memories = [
            {
                "id": item.id,
                "text": item.text,
                "type": item.type,
                "context": item.context,
                "occurred_start": item.occurred_start,
                "occurred_end": item.occurred_end,
                "metadata": item.metadata,
                "tags": item.tags,
            }
            for item in recalled.results
        ]

        reflect_query = (
            "Based only on the team's remembered engineering experiences, what "
            "should the team do for this upcoming change? Identify relevant past "
            "outcomes, what worked or failed, and concrete safeguards. Do not "
            "invent experience. Upcoming change: "
            + json.dumps(change)
        )

        reflection = await self.memory.reflect(reflect_query)

        prompt = f"""
You are an engineering change advisor.

Upcoming change:
{json.dumps(change, indent=2)}

Hindsight recalled memories:
{json.dumps(memories, indent=2)}

Hindsight reflection:
{reflection}

Return JSON with exactly these fields:
- recommendation
- rollout_strategy
- safeguards (array)
- evidence (array)
- uncertainty
- why_memory_changed_the_recommendation

Rules:
1. Only claim evidence that appears in the Hindsight memories or reflection.
2. Do not invent previous incidents, outcomes, or lessons.
3. If there are no relevant memories, explicitly say that there is no
   team-specific historical evidence.
4. Evidence should refer to the actual remembered experience, not internal
   SDK object representations.
"""

        response = await self.llm.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "You are precise and evidence-grounded.",
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            temperature=0.1,
            response_format={"type": "json_object"},
        )

        result = json.loads(response.choices[0].message.content)

        result["change_id"] = change_id

        # Memory is considered used only when Hindsight returned
        # at least one recalled result.
        result["memory_used"] = len(memories) > 0
        result["memory_count"] = len(memories)

        result["memory_evidence"] = [
            {
                "memory_id": item["id"],
                "type": item["type"],
                "summary": item["text"],
                "context": item["context"],
                "occurred_start": item["occurred_start"],
                "occurred_end": item["occurred_end"],
            }
            for item in memories
        ]

        return result

    async def record_outcome(self, outcome: dict):
        content = (
            f"Engineering change outcome for {outcome['change_id']}. "
            f"Outcome: {outcome['outcome']}. "
            f"Impact: {outcome.get('impact', '')}. "
            f"Root cause: {outcome.get('root_cause', '')}. "
            f"Resolution: {outcome.get('resolution', '')}. "
            f"Lessons learned: {outcome.get('lessons_learned', '')}."
        )

        await self.memory.retain(
            content=content,
            context="engineering change outcome",
            metadata={"change_id": outcome["change_id"]},
            tags=["engineering-change", "outcome"],
        )

        return {
            "status": "retained",
            "change_id": outcome["change_id"],
        }