from sqlalchemy.orm import Session
from app.models.users import User, AccountVerification
from typing import Dict, Any


def add_user(session: Session, user_info: Dict[str, Any]):
    user_item = User(**user_info)
    session.add(user_item)


def add_account_verification(session: Session, verification_info: Dict[str, Any]):
    verification_item = AccountVerification(**verification_info)
    session.add(verification_item)


def update_verified_status(session: Session, phone_number: str, status: bool):
    session.query(User).filter(User.phone_number == phone_number).update(
        {"is_verified": status}
    )


def get_user_verification(session: Session, otp: str) -> AccountVerification:
    acc_verification = (
        session.query(AccountVerification)
        .filter(AccountVerification.token == otp)
        .first()
    )
    return acc_verification
