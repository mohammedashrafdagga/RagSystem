from pydantic_settings import BaseSettings, SettingsConfigDict


# Setting Loading into Settings
class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str
    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNK_SIZE: int

    MONGODB_URI: str
    MONGODB_DATABASE_NAME: str

    class Config:
        env_file = ".env"


# return object from Settings
def get_settings():
    return Settings()
