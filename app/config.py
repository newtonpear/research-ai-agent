from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""

    app_name: str = "Research AI Agent"
    app_env: str = "development"
    app_host: str = "127.0.0.1"
    app_port: int = 8000

    openai_api_key: str
    openai_base_url: str = "https://api.openai.com/v1"
    model_name: str = "gpt-4o-mini"

    log_level: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
