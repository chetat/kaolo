from fastapi import APIRouter
from app.api.v1.users.auth import router as auth_router
from app.api.v1.users.profile import router as profile_router
from app.api.v1.users.address import router as address_router

api_router = APIRouter()

api_router.include_router(auth_router, tags=["Authentication"], prefix="/users")
api_router.include_router(profile_router, tags=["Profile"], prefix="/users")
api_router.include_router(address_router, tags=["Address"], prefix="/users")
