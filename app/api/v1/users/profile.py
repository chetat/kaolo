from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_session

router = APIRouter()


# Note: Why choose int over str for user_id?
# String is faster for db queries because it takes less space (less 4 bytes) to store
# Compare to uuid(str 16 bytes)
@router.get("/{user_id}")
async def get_user_info(user_id: str, session: Session = Depends(get_session)):
    return {"message": f"Hello {user_id}"}


@router.patch("/{user_id}")
async def update_user_info(user_id: str, session: Session = Depends(get_session)):
    return {"message": f"Hello {user_id}"}
