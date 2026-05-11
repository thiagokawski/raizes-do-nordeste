from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class ConnectionSettings(BaseSettings):
    DATABASE_URL: str = ""

    model_config = ConfigDict(
        env_file=".env",
        extra="ignore"
    )


DATABASE_URL = ConnectionSettings().DATABASE_URL

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()