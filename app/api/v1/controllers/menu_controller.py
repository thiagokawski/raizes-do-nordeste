from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.infrastructure.database.database_connection import get_db

router = APIRouter(
    prefix="/menu",
    tags=["MENUS"]
)

@router.get(
        "/{id_menu}", 
        response_model=str
    )
def get_menu(
    id_menu: int, 
    db: Session = Depends(get_db)
):
    return 'ok'