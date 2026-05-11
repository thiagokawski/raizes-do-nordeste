from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class SecuritySettings(BaseSettings):
    JWT_SECRET_KEY: str = ""
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 60

    model_config = ConfigDict(
        env_file=".env",
        extra="ignore"
    )

security_settings = SecuritySettings()