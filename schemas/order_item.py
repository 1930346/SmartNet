from pydantic import BaseModel


class Order_item(BaseModel):
    id: str | None = None
    order_id: str
    product_id: str
    quantity: str