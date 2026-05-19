from app.agent.memory import get_project_memory
from app.agent.prompts import build_research_prompt
from app.services.llm_service import LLMService


class ResearchAgent:
    """Main research agent.

    Current capability:
    - chat with an OpenAI-compatible LLM;
    - inject project-specific memory for WRF wildfire research;
    - generate research-oriented answers.

    Future extensions:
    - paper search;
    - GitHub repository search;
    - scheduled literature monitoring;
    - vector memory;
    - WeChat integration.
    """

    def __init__(self) -> None:
        self.llm_service = LLMService()

    async def run(self, user_message: str) -> str:
        """Run the agent with a user message."""
        project_memory = get_project_memory(topic=user_message)
        system_prompt = build_research_prompt(project_memory)

        return await self.llm_service.generate_response(
            system_prompt=system_prompt,
            user_message=user_message,
        )
