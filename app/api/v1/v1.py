from fastapi import APIRouter

from .controllers import router_user

router = APIRouter(prefix="/v1")

router.include_router(router_user, tags=["USUÁRIOS"])