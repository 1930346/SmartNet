from pydantic import BaseModel

class Order_detail(BaseModel):
    id: str | None = None
    user_id: str 
    payment_id: str
    total: float
    created_at: str | None = None