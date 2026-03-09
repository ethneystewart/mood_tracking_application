from fastapi import APIRouter
from models.request_models import MoodLogCreate
from services.moodlog_service import create_moodlog, get_moodlogs

router = APIRouter(prefix="/moodlogs", tags=["MoodLogs"])


@router.get("/")
def get_moodlogs_route():
    return get_moodlogs()


@router.post("/")
def create_moodlog_route(log: MoodLogCreate):

    return create_moodlog(
        log.date,
        log.sleepHours,
        log.energyLevels,
        log.activities,
        log.tags,
        log.user_id
    )