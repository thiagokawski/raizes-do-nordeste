from fastapi import APIRouter

from .controllers import router_auth, router_menu, router_order

router = APIRouter(prefix="/v1")

router.include_router(router_auth)
router.include_router(router_menu)
router.include_router(router_order)
