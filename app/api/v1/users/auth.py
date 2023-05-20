from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_session
from app.schemas.users import UserRequest
from app.services import users as user_service
from app.services import messages as message_service
from app.logger.kaolog import get_logger

logger = get_logger(__name__)
router = APIRouter()


@router.post("")
def create_user(user_request: UserRequest, session: Session = Depends(get_session)):
    password = user_request.password
    user_request_dict = user_request.dict(exclude={"password"})
    try:
        otp = message_service.generate_otp()
        user_service.create_user(session, password, user_request_dict, otp)
        message_service.send_otp_sms(user_request.phone_number, otp)
        return {"message": "User created"}
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "message": "Something went wrong when creating user",
            },
        )


@router.post("/verify")
def verify_user(otp: str, session: Session = Depends(get_session)):
    try:
        is_verified = user_service.verify_user(session, otp)
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "message": "Something went wrong when verifying user",
            },
        )

    if not is_verified:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "message": "Invalid OTP",
            },
        )

    return {"message": "User verified"}


@router.get("/access-token")
async def authenticate_user(user_id: str, session: Session = Depends(get_session)):
    return {"message": f"Hello {user_id}"}


@router.post("/logout")
async def logout_user(session: Session = Depends(get_session)):
    return {"message": "Logged Out"}
