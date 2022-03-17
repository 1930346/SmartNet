from pydantic import BaseModel

class Payment_detail(BaseModel):
    id: str | None = None
    order_id: str
    provider: str
    amount: float