from passlib.context import CryptContext
from uuid import uuid4
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def generate_public_id() -> str:
    uid_striped = str(uuid4()).split("-")
    return "".join(uid_striped)[:30]

def generate_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
