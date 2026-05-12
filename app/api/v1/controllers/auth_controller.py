from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.infrastructure.database.database_connection import get_db
from app.infrastructure.repositories.sql_user_repository import SqlUserRepository
from app.core.security.password_hasher import PasswordHasher
from app.core.security.jwt_provider import JwtProvider
from app.application.use_cases.auth.login_user_use_case import LoginUserUseCase
from app.api.v1.schemas.auth_schema import LoginRequest, LoginResponse
from app.api.v1.schemas.api_default_schema import ResponseDefault

router = APIRouter(
    prefix="/auth",
    tags=["AUTH"]
)

@router.post("/login", response_model=ResponseDefault[LoginResponse])
def login(
    request: LoginRequest, 
    db: Session = Depends(get_db)
):    
    use_case = LoginUserUseCase(
        user_repository=SqlUserRepository(db),
        password_hasher=PasswordHasher(),
        jwt_provider=JwtProvider()
    )

    return ResponseDefault.success(
        data=use_case.execute(
            email=request.email,
            password=request.password
        ),
        message="Login executado com sucesso!"
    )
