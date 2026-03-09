from fastapi import APIRouter
from models.request_models import UserCreate
from services.user_service import create_user, get_users

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
def get_users_route():
    return get_users()


@router.post("/")
def create_user_route(user: UserCreate):
    return create_user(
        user.firstName,
        user.lastName,
        user.email
    )