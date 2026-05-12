from pydantic import BaseModel, Field

class CreateOrderReq(BaseModel):
    id_item: int = Field(gt=0)
    amount: int = Field(gt=0)


class OrderResponse(BaseModel):
    id_order: int
    price: float
    status: str
    source: str
