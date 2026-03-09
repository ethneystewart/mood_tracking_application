from fastapi import APIRouter
from models.request_models import MoodCreate
from services.mood_service import create_mood, get_moods

router = APIRouter(prefix="/mood", tags=["Moods"])

#get all moods 
@router.get("/moods")
def get_moods_route():
    return get_moods()

#create a new mood 
@router.post("/moods")
def create_mood_route(mood: MoodCreate):
    return create_mood(
        mood.mood,
        mood.sentiment,
        mood.moodlog_id
    )