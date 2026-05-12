from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.v1.dependencies.auth_dependencies import get_current_user
from app.api.v1.schemas.api_default_schema import ResponseDefault
from app.api.v1.schemas.menu_schema import MenuResponse, MenuResponseBasic
from app.application.use_cases.menu.get_menu_by_id_use_case import GetMenuByIdUseCase
from app.infrastructure.database.database_connection import get_db
from app.infrastructure.repositories.sql_menu_repository import SqlMenuRepository

router = APIRouter(
    prefix="/menus",
    tags=["MENUS"]
)

@router.get(
    "/{id_menu}", 
    response_model=ResponseDefault[MenuResponse],
    dependencies=[Depends(get_current_user)]
)
def get_menu_by_id(
    id_menu: int, 
    db: Session = Depends(get_db)
):
    use_case = GetMenuByIdUseCase(
        menu_repository=SqlMenuRepository(db)
    )

    return ResponseDefault.success(
        data=use_case.execute(id_menu=id_menu),
        message="Cardápio retornado com sucesso!"
    )