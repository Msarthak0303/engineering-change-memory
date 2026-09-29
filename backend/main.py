import os

from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

from agent.change_agent import ChangeAgent
from hindsight.adapter import HindsightMemory


memory = HindsightMemory()
agent = ChangeAgent(memory)


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await memory.close()


app = FastAPI(
    title="Engineering Change Memory",
    version="0.1.0",
    lifespan=lifespan,
)


class ChangeRequest(BaseModel):
    service: str
    change_type: str
    summary: str
    environment: str = "staging"
    timing: str = "business-hours"
    risk_context: str = ""


class OutcomeRequest(BaseModel):
    change_id: str
    outcome: str
    impact: str = ""
    root_cause: str = ""
    resolution: str = ""
    lessons_learned: str = ""


@app.get("/")
async def frontend():
    frontend_path = Path(__file__).resolve().parent.parent / "frontend" / "index.html"
    return FileResponse(frontend_path)


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "service": "engineering-change-memory",
        "memory_backend": os.getenv("HINDSIGHT_BASE_URL", "http://localhost:8888"),
        "llm_model": os.getenv("LLM_MODEL", "openai/gpt-oss-120b"),
    }


@app.post("/analyze")
async def analyze_change(change: ChangeRequest):
    return await agent.analyze(change.model_dump())


@app.post("/outcome")
async def record_outcome(outcome: OutcomeRequest):
    return await agent.record_outcome(outcome.model_dump())
