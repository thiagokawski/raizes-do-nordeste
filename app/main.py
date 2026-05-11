from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from app.core.handler.schema_validation_exception import validation_exception_handler

from .api import router_v1

app = FastAPI()

app.add_exception_handler(RequestValidationError, validation_exception_handler)

app.include_router(router_v1, prefix="/api")