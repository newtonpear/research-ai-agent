from fastapi import FastAPI, HTTPException

from app.agent.core import ResearchAgent
from app.config import settings
from app.schemas import AgentRequest, AgentResponse, HealthResponse
from app.utils.logger import get_logger

logger = get_logger(__name__)

app = FastAPI(
    title=settings.app_name,
    description="A lightweight AI agent backend for research assistance.",
    version="0.1.0",
)

agent = ResearchAgent()


@app.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """Check whether the service is running."""
    return HealthResponse(
        status="ok",
        app_name=settings.app_name,
        environment=settings.app_env,
    )


@app.post("/agent/chat", response_model=AgentResponse)
async def chat_with_agent(request: AgentRequest) -> AgentResponse:
    """Send a user message to the AI agent and return its response."""
    try:
        logger.info("Received agent request.")
        response = await agent.run(request.message)
        return AgentResponse(response=response)
    except Exception as exc:
        logger.exception("Agent execution failed.")
        raise HTTPException(
            status_code=500,
            detail=f"Agent execution failed: {exc}",
        ) from exc
