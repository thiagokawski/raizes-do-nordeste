from fastapi import APIRouter

router = APIRouter(prefix="/user")

@router.get("/teste")
def teste():
    return "ok"