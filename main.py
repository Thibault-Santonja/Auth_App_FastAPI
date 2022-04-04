#!/usr/bin/env python3.10
import uvicorn
from fastapi import FastAPI


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

    uvicorn.run(app, host="localhost", port=3200)
