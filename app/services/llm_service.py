from openai import AsyncOpenAI

from app.config import settings


class LLMService:
    """OpenAI-compatible LLM service wrapper."""

    def __init__(self) -> None:
        self.client = AsyncOpenAI(
            api_key=settings.openai_api_key,
            base_url=settings.openai_base_url,
        )
        self.model_name = settings.model_name

    async def generate_response(
        self,
        system_prompt: str,
        user_message: str,
    ) -> str:
        """Generate a response from the configured language model."""
        completion = await self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_message,
                },
            ],
            temperature=0.3,
        )

        content = completion.choices[0].message.content

        if content is None:
            return "No response was generated."

        return content
