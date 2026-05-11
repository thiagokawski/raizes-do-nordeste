from typing import Generic, TypeVar
from pydantic import BaseModel, Field

T1 = TypeVar("T1")

class ResponseDefault(BaseModel, Generic[T1]):
    status: int = Field(default=200)
    message: str = Field(default="Sucesso")
    data: T1 | None = None

    @classmethod
    def success(cls, data: T1, message: str = "Sucesso"):
        return cls(
            status=200,
            message=message,
            data=data
        )

    @classmethod
    def created(cls, data: T1, message: str = "Criado com sucesso"):
        return cls(
            status=201,
            message=message,
            data=data
        )