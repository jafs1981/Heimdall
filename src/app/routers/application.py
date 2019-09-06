from fastapi import APIRouter, Depends, HTTPException


router = APIRouter()

# ---------------------------------------------------------------------------------------
# GET SAMPLE
# ---------------------------------------------------------------------------------------
@router.get("/application", tags=["v1"])
async def list_application_definitions():
    return {"msg": "hello"}


# ---------------------------------------------------------------------------------------
# GET SINGLE APPLICATION
# ---------------------------------------------------------------------------------------
@router.get("/application/{application_id}", tags=["v1"])
async def list_application_definitions(application_id: str):
    return {"msg": "hello"}

