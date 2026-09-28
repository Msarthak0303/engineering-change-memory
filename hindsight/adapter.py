import os

from hindsight_client import Hindsight


class HindsightMemory:
    def __init__(self):
        self.client = Hindsight(
            base_url=os.getenv(
                "HINDSIGHT_BASE_URL",
                "http://localhost:8888",
            ),
            api_key=os.getenv("HINDSIGHT_API_KEY") or None,
        )
        self.bank_id = os.getenv(
            "HINDSIGHT_BANK_ID",
            "engineering-team",
        )

    async def retain(self, content: str, **kwargs):
        return await self.client.aretain(
            bank_id=self.bank_id,
            content=content,
            **kwargs,
        )

    async def recall(self, query: str):
        return await self.client.arecall(
            bank_id=self.bank_id,
            query=query,
        )

    async def reflect(self, query: str):
        return await self.client.areflect(
            bank_id=self.bank_id,
            query=query,
        )

    async def close(self):
        await self.client.aclose()