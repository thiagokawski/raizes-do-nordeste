from fastapi import APIRouter

from .controllers import router_auth, router_menu

router = APIRouter(prefix="/v1")

router.include_router(router_auth)
router.include_router(router_menu)