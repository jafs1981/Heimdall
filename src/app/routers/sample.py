from fastapi import APIRouter, Depends, HTTPException


router = APIRouter()

# ---------------------------------------------------------------------------------------
# GET SAMPLE
# ---------------------------------------------------------------------------------------
@router.get("/sample}", tags=["sample"])
async def get_skill():
    return {"msg": "hello"}

