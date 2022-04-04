from fastapi import APIRouter

from server.settings.fast_api import settings


router = APIRouter()


@router.on_event("startup")
async def startup_event():
    return {"result": "Hi there !"}


@router.on_event("shutdown")
async def shutdown_event():
    return {"result": "See ya !"}


@router.get("/", include_in_schema=False)
def home():
    return {"result": "Hello !"}


@router.get("/info")
async def info():
    """
    Returns app information. <br />
    :return: Return a JSON with the app name and admin email
    """
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email
    }
