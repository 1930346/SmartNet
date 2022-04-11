from pydantic import BaseModel, Field

# Modelo base
# class Order_item(BaseModel):
#     # id: str | None = None
#     order_id: str
#     product_id: str
#     quantity: str

class Order_item(BaseModel):
    order_id: str = Field(title="The id of the order")
    product_id: str = Field(title="The id of the product")
    quantity: str = Field(title="The quantity of the product")

class Order_item_outs(Order_item):
    id: str = Field(title="The id of the order item")

class Order_item_in(Order_item):
    pass

class Order_item_update(Order_item):
    pass