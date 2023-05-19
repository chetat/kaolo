from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from app.core.settings import Settings, get_settings
from contextlib import contextmanager

settings: Settings = get_settings()

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(engine)


def get_session() -> SessionLocal:
    try:
        db_session = SessionLocal()
        yield db_session
    except SQLAlchemyError as error:
        db_session.rollback()
        raise error
    finally:
        db_session.close()
