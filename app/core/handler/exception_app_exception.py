from fastapi import Request
from fastapi.responses import JSONResponse
from app.api.v1.schemas.api_default_schema import ResponseDefault

# CLASSE USADA PARA LANÇAR EXEÇÕES PADRONIZADAS NO RESPONSE
class AppException(Exception):
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code


async def handler_app_exception(request: Request, exc: AppException):   
    response = ResponseDefault(
        status=exc.status_code,
        message=exc.message,
        data=None
    )

    return JSONResponse(
        status_code=exc.status_code,
        content=response.model_dump()
    )