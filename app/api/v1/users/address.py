from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_session

router = APIRouter()


@router.post("/address/{user_id}/{address_id}")
async def create_user_address(
    user_id: str, address_id: str, session: Session = Depends(get_session)
):
    return {"message": f"Hello create address{user_id} {address_id}"}


# Note: Why choose int over str for user_id?
@router.get("/address/{user_id}")
async def get_user_addresses(user_id: str, session: Session = Depends(get_session)):
    return {"message": f"Hello fetch address {user_id}"}


@router.patch("/address/{user_id}")
async def update_user_address(user_id: str, session: Session = Depends(get_session)):
    return {"message": f"Hello update address {user_id}"}
