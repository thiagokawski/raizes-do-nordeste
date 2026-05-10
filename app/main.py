from fastapi import FastAPI

from .api import router_v1

app = FastAPI()

app.include_router(router_v1, prefix="/api")