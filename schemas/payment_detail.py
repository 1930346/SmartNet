from pydantic import BaseModel

# Modelo base
# class Payment_detail(BaseModel):
#     # id: str | None = None
#     order_id: str
#     provider: str
#     amount: float

class Payment_detail(BaseModel):
    order_id: str
    provider: str
    amount: float


class Payment_detail_outs(Payment_detail):
    id: str

class Payment_detail_in(Payment_detail):
    pass

class Payment_detail_update(Payment_detail):
    pass