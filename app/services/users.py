from sqlalchemy.orm import Session
from typing import Dict, Any
from app.helpers.password import generate_password_hash, generate_public_id
from app.repository import user as user_repo
from datetime import datetime, timedelta


def create_user(session: Session, password, user_info: Dict[str, Any], otp: str):
    user_info["password_hash"] = generate_password_hash(password)
    user_info["public_id"] = generate_public_id()
    user_repo.add_user(session, user_info)
    verification_info = {"token": otp, "phone_number": user_info["phone_number"]}
    user_repo.add_account_verification(session, verification_info)
    session.commit()


def create_account_verification(session: Session, verification_info: Dict[str, Any]):
    user_repo.add_account_verification(session, verification_info)
    session.commit()


def verify_user(session: Session, otp: str):
    is_verified = True
    acc_verifcation = user_repo.get_user_verification(session, otp)
    is_expired = acc_verifcation.created_at + timedelta(minutes=5) < datetime.utcnow()
    if not acc_verifcation or is_expired:
        return False

    update_verification_status(session, acc_verifcation.phone_number, is_verified)
    session.commit()
    return True


def update_verification_status(session: Session, phone_number: str, status: bool):
    user_repo.update_verified_status(session, phone_number, status)
    session.commit()


def get_user_by_id(user_id: str):
    return {"message": f"Hello {user_id}"}


def logout_user():
    return {"message": "Logged Out"}


def authenticate_user(user_id: str):
    return {"message": f"Hello {user_id}"}


def update_user_info(session: Session, user_id: str, user_info: Dict[str, Any]):
    return {"message": f"Hello {user_id}"}


def get_user_addresses(user_id: str):
    return {"message": f"Hello fetch address {user_id}"}


def update_user_address(user_id: str):
    return {"message": f"Hello update address {user_id}"}


def create_user_address(user_id: str, address_id: str):
    return {"message": f"Hello create address{user_id} {address_id}"}


def change_password(user_id: str, old_password: str, new_password: str):
    return {"message": f"Hello change password {user_id}"}


def reset_password(user_id: str, new_password: str):
    return {"message": f"Hello reset password {user_id}"}
