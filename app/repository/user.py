from sqlalchemy.orm import Session
from app.models.users import User
from typing import Dict, Any


def add_user(session: Session, user_info: Dict[str, Any]):
    user_item = User(**user_info)
    session.add(user_item)
