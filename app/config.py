from pydantic_settings import BaseSettings
from pydantic import PostgresDsn

class Config(BaseSettings):
    DATABASE_URL: PostgresDsn
    JWT_SECRET: str = "your-secret-key-change-this"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRY_MINUTES: int = 60
    LLM_API_URL: str = "http://external-llm-api.com/summary"  # Placeholder for external LLM API
    LLM_API_KEY: str = "your-llm-api-key"  # Placeholder for LLM API key

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Config()