from datetime import datetime, timedelta, timezone
from typing import Any

from jose import jwt

from app.core.settings.security_settings import security_settings


class JwtProvider:

    def create_access_token(self, data: dict[str, Any]) -> str:
        payload = data.copy()
        now = datetime.now(timezone.utc)

        expire = now + timedelta(
            minutes=security_settings.JWT_EXPIRE_MINUTES
        )

        payload.update({
            "exp": expire,
            "iat": now,
            "type": "access",
        })

        return jwt.encode(
            payload,
            security_settings.JWT_SECRET_KEY,
            algorithm=security_settings.JWT_ALGORITHM
        )
