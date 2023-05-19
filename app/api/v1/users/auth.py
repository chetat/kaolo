from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_session
from app.schemas.users import UserRequest
from app.services import users as user_service
from app.logger.kaolog import get_logger

logger = get_logger(__name__)
router = APIRouter()

@router.post("")
async def create_user(
    user_request: UserRequest, session: Session = Depends(get_session)
):
    password = user_request.password
    user_request_dict = user_request.dict(exclude={"password"})
    try:
        user_service.create_user(session, password, user_request_dict)
        return {"message": "User created"}
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={ 
                "message": "Something went wrong when creating user",
            }
        )


@router.get("/access-token")
async def authenticate_user(user_id: str, session: Session = Depends(get_session)):
    return {"message": f"Hello {user_id}"}



@router.post("/logout")
async def logout_user(session: Session = Depends(get_session)):
    return {"message": "Logged Out"}
