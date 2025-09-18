from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    api_name: str = Field(default="appsec-demo")
    api_key: str | None = None  # se puede usar para auth en el futuro

    # Configuración moderna de Pydantic v2
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

def get_settings() -> Settings:
    return Settings()

