from fastapi import Request
from fastapi.responses import JSONResponse
from app.api.v1.schemas.api_default_schema import ResponseDefault


async def handler_global_exception(request: Request, exc: Exception):   
    response = ResponseDefault(
        status=500,
        message=str(exc),
        data=None
    )

    return JSONResponse(
        status_code=500,
        content=response.model_dump()
    )