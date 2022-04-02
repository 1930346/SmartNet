from pydantic import BaseModel
from datetime import datetime

class Order_detail(BaseModel):
    # id: str | None = None
    user_id: str 
    payment_id: str
    total: float
    # created_at: datetime | None = None