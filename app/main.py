from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from app.core.handler.exception_schema_validation import handler_validation_schema
from app.core.handler.exception_global_exception import handler_global_exception
from app.core.handler.exception_app_exception import AppException, handler_app_exception

from .api import router_v1

app = FastAPI()

# HANDDLERS
app.add_exception_handler(RequestValidationError, handler_validation_schema)    # status_code = 422
app.add_exception_handler(AppException, handler_app_exception)                  # status_code = todos que não sejam de sucesso, mas sejam esperados, ex: 401, 403, 404
app.add_exception_handler(Exception, handler_global_exception)                  # status_code = 500

app.include_router(router_v1, prefix="/api")