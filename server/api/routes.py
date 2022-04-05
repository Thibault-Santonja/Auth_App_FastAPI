from datetime import timedelta

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from server.api.exceptions import INCORRECT_CREDENTIALS
from server.db.db import get_db
from server.security.token import create_access_token
from server.crud.user import authenticate_user
from server.settings.fast_api import settings
from server.settings.variables import ACCESS_TOKEN_EXPIRE_MINUTES
from server.schemas.Token import Token

router = APIRouter()


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


@router.post("/auth/login", tags=["authentication"], response_model=Token)
def login_for_access_token(
        db: Session = Depends(get_db),
        form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Login function returns an access token if user is identified. <br />
    :param db: Get database Session <br />
    :param form_data: Get form data (username & password) <br />
    :return: Return a JSON token with the type and the token itself
    """
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise INCORRECT_CREDENTIALS

    access_token = create_access_token(
        data={
            "user_id": str(user.id),
            "user_name": user.username,
            "is_admin": str(user.is_admin).lower(),
        },
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    return {"access_token": access_token, "token_type": "bearer"}  # PlainTextResponse(access_token)
