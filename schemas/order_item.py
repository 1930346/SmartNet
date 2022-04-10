from pydantic import BaseModel

# Modelo base
# class Order_item(BaseModel):
#     # id: str | None = None
#     order_id: str
#     product_id: str
#     quantity: str

class Order_item(BaseModel):
    order_id: str
    product_id: str
    quantity: str

class Order_item_outs(Order_item):
    id: str

class Order_item_in(Order_item):
    pass

class Order_item_update(Order_item):
    pass