from pydantic import BaseModel, Field

# Modelo base
# class Payment_detail(BaseModel):
#     # id: str | None = None
#     order_id: str
#     provider: str
#     amount: float

class Payment_detail(BaseModel):
    # order_id: str = Field(title="The id of the order")
    provider: str = Field(title="The provider of the payment")
    amount: float = Field(title="The amount of the payment")


class Payment_detail_outs(Payment_detail):
    id: str = Field(title="The id of the payment")

class Payment_detail_in(Payment_detail):
    pass

class Payment_detail_update(Payment_detail):
    pass