from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "SENTINEL"
    debug: bool = False
    gemini_api_key: str = ""
    database_url: str = ""

    class Config:
        env_file = ".env"


settings = Settings()

