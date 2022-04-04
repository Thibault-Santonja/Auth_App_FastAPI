#!/usr/bin/env python3.10
import uvicorn
from fastapi import FastAPI

from server.settings.variables import API_HOST, API_PORT
from server.db.db import engine
from server.db.model import Base


if __name__ == "__main__":
    app = FastAPI(
        title="Amanogawa",
        description="Template app",
        version="0.1.0",
        license_info={
            "name": "MIT",
            "url": "https://opensource.org/licenses/MIT",
        }
    )
    Base.metadata.create_all(bind=engine)

    uvicorn.run(app, host=API_HOST, port=API_PORT)
