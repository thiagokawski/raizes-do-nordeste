from fastapi import APIRouter

from .controllers import router_auth

router = APIRouter(prefix="/v1")

router.include_router(router_auth)