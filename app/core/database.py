from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.settings import Settings, get_settings
from contextlib import contextmanager

settings: Settings = get_settings()

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(engine)


@contextmanager
def get_session():
    try:
        db_session = SessionLocal()
        yield db_session
    finally:
        db_session.close()
