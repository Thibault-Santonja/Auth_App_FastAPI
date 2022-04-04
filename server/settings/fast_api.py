from fastapi import FastAPI
from pydantic import BaseSettings


APP_NAME = "Auth_App"
APP_VERSION = "0.1.0"
CONTACT_MAIL = "thibault.santonja@gmail.com"
CONTACT = {
    "name": "Thibault Santonja",
    "url": "https://github.com/Thibault-Santonja",
    "email": CONTACT_MAIL,
}
DESCRIPTION = f"""
{APP_NAME} API v{APP_VERSION}. 🚀

## Users
todo
"""
LICENSE = {
    "name": "MIT",
    "url": "https://opensource.org/licenses/MIT",
}
TAGS_METADATA = [
    {
        "name": "default",
        "description": "Some basic routes.",
    },
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    },
]

app = FastAPI(
    title="Amanogawa",
    description="Template app",
    version="0.1.0",
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    }
)


class Settings(BaseSettings):
    app_name: str = APP_NAME
    admin_email: str = CONTACT_MAIL


settings = Settings()
