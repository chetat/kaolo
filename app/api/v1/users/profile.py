from fastapi import FastAPI, APIRouter

router = APIRouter()

# Note: Why choose int over str for user_id?
@router.get("/{user_id}")
async def get_user_info(user_id: str):
    return {"message": f"Hello {user_id}"}

@router.patch("/{user_id}")
async def update_user_info(user_id: str):
    return {"message": f"Hello {user_id}"}