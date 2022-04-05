#!/usr/bin/env python3.10
import uvicorn

from server.settings.variables import API_HOST, API_PORT, API_ROOT
from server.settings.fast_api import app
from server.db.db import engine
from server.db import Base
from server.api import routes


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)

    app.include_router(routes.router, prefix=API_ROOT, tags=["default"])

    uvicorn.run(app, host=API_HOST, port=API_PORT)
