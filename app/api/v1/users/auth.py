from fastapi import FastAPI, APIRouter

router = APIRouter()


# Note: Why choose int over str for user_id?
@router.get("/login")
async def authenticate_user(user_id: str):
    return {"message": f"Hello {user_id}"}


@router.post("")
async def create_user():
    return {"message": "User created"}


@router.post("/logout")
async def logout_user():
    return {"message": "Logged Out"}