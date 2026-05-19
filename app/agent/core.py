from app.agent.prompts import SYSTEM_PROMPT
from app.services.llm_service import LLMService


class ResearchAgent:
    """Main research agent.

    This class is intentionally lightweight.
    More tools can be added later, for example:
    - paper search
    - GitHub search
    - scheduled literature monitoring
    - vector memory
    - WeChat integration
    """

    def __init__(self) -> None:
        self.llm_service = LLMService()

    async def run(self, user_message: str) -> str:
        """Run the agent with a user message."""
        return await self.llm_service.generate_response(
            system_prompt=SYSTEM_PROMPT,
            user_message=user_message,
        )
