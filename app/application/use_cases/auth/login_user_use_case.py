from fastapi import HTTPException, status

from app.domain.repositories.user_repository import UserRepository
from app.core.security.password_hasher import PasswordHasher
from app.core.security.jwt_provider import JwtProvider
from app.api.v1.schemas.auth_schema import LoginResponse


class LoginUserUseCase:

    def __init__(
        self,
        user_repository: UserRepository,
        password_hasher: PasswordHasher,
        jwt_provider: JwtProvider
    ):
        self.user_repository = user_repository
        self.password_hasher = password_hasher
        self.jwt_provider = jwt_provider

    def execute(self, email: str, password: str) -> LoginResponse:
        user = self.user_repository.find_by_email(email)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Email ou senha inválidos"
            )

        if not user.active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Usuário inativo"
            )

        password_is_valid = self.password_hasher.verify(
            plain_password=password,
            hashed_password=user.password
        )

        if not password_is_valid:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Email ou senha inválidos"
            )

        token = self.jwt_provider.create_access_token(
            {
                "sub": str(user.id_user),
                "email": user.email,
                "name": user.name,
            }
        )

        return LoginResponse(
            access_token=token,
            user_id=user.id_user,
            name=user.name,
            email=user.email,
        )
