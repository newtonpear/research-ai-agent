from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """Response schema for health check endpoint."""

    status: str
    app_name: str
    environment: str


class AgentRequest(BaseModel):
    """Request schema for sending a message to the agent."""

    message: str = Field(
        ...,
        min_length=1,
        description="User message sent to the AI agent.",
        examples=["Recommend recent research directions about WRF wildfire modelling."],
    )


class AgentResponse(BaseModel):
    """Response schema returned by the agent."""

    response: str
