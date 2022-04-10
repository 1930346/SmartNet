from pydantic import BaseModel
from datetime import datetime

# Modelo base
# class Order_detail(BaseModel):
#     # id: str | None = None
#     user_id: str 
#     payment_id: str
#     total: float
#     # created_at: datetime | None = None

class Order_detail(BaseModel):
    user_id: str 
    payment_id: str
    total: float

class Order_detail_in(Order_detail):
    pass

class Order_detail_outs(Order_detail):
    id: str
    created_at: datetime

class Order_detail_update(Order_detail):
    pass