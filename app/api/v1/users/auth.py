from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_session

router = APIRouter()


# Note: Why choose int over str for user_id?
@router.get("/login")
async def authenticate_user(user_id: str, session: Session = Depends(get_session)):
    return {"message": f"Hello {user_id}"}


@router.post("")
async def create_user(session: Session = Depends(get_session)):
    return {"message": "User created"}


@router.post("/logout")
async def logout_user(session: Session = Depends(get_session)):
    return {"message": "Logged Out"}
