from fastapi import APIRouter
from models.request_models import ReflectionCreate
from services.reflections_service import create_reflection, get_reflections

router = APIRouter(prefix="/reflection", tags=["Reflections"])


# create a new reflection
@router.post("/reflections")
def create_reflection_route(reflection: ReflectionCreate):
    return create_reflection(
        reflection.reflection,
        reflection.moodlog_id
    )

#get reflections for a specific mood log
@router.get("/reflections/{moodlog_id}")
def get_reflections_route(moodlog_id: int):
    return get_reflections(moodlog_id)