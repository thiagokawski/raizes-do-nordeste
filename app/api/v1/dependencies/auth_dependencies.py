from fastapi import Depends, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError
from sqlalchemy.orm import Session

from app.core.handler.exception_app_exception import AppException
from app.core.security.jwt_provider import JwtProvider
from app.domain.entities.user import User
from app.infrastructure.database.database_connection import get_db
from app.infrastructure.repositories.sql_user_repository import SqlUserRepository

bearer_scheme = HTTPBearer(auto_error=False)


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: Session = Depends(get_db)
) -> User:
    if not credentials:
        raise AppException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            message="Usuário não autenticado"
        )

    try:
        payload = JwtProvider().decode_access_token(credentials.credentials)
    except JWTError:
        raise AppException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            message="Token inválido ou expirado"
        )

    if payload.get("type") != "access":
        raise AppException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            message="Token inválido ou expirado"
        )

    id_user = payload.get("sub")

    if not id_user:
        raise AppException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            message="Token inválido ou expirado"
        )

    try:
        id_user = int(id_user)
    except ValueError:
        raise AppException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            message="Token inválido ou expirado"
        )

    user = SqlUserRepository(db).find_by_id(id_user)
    if not user:
        raise AppException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            message="Usuário não autenticado"
        )

    if not user.active:
        raise AppException(
            status_code=status.HTTP_403_FORBIDDEN,
            message="Usuário inativo"
        )

    return user
