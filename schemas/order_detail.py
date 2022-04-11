from pydantic import BaseModel, Field
from datetime import datetime

# Modelo base
# class Order_detail(BaseModel):
#     # id: str | None = None
#     user_id: str 
#     payment_id: str
#     total: float
#     # created_at: datetime | None = None

class Order_detail(BaseModel):
    user_id: str = Field(title="The id of the user")
    payment_id: str = Field(title="The id of the payment")
    total: float = Field(title="The total of the order")

class Order_detail_in(Order_detail):
    pass

class Order_detail_outs(Order_detail):
    id: str = Field(title="The id of the order")
    created_at: datetime = Field(title="The date of creation of the order")

class Order_detail_update(Order_detail):
    pass