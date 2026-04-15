from fastapi import APIRouter
from database.crud import get_analyses

router = APIRouter()

@router.get("/analyses")
def fetch_analyses():
    data = get_analyses()

    return {
        "analyses": data
    }