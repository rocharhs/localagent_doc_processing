from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
async def test():
    return "Everything A-OK"
