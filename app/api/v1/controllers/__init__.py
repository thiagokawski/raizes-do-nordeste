from .auth_controller import router as router_auth
from .menu_controller import router as router_menu
from .order_controller import router as router_order


__all__ = [
    "router_auth",
    "router_menu",
    "router_order"
]
