from .auth_controller import router as router_auth
from .menu_controller import router as router_menu


__all__ = [
    "router_auth",
    "router_menu"
]