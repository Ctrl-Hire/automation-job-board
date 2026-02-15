from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = "postgresql+psycopg://aitb:aitb_dev_password@localhost:5432/aitb_jobboard"

    # Auth
    JWT_SECRET_KEY: str = "hackathon-secret-key-change-later"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours for hackathon convenience

    # OpenRouter
    OPENROUTER_API_KEY: str = ""

    # App
    DEBUG: bool = True

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
