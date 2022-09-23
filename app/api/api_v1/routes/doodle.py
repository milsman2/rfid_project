from fastapi import APIRouter

router = APIRouter()

@router.post("/number_2")
async def number_2():
    return {"status": "ok"}