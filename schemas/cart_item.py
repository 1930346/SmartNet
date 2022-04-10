from pydantic import BaseModel
from datetime import datetime

# Modelo base
# class Cart_item(BaseModel):
#     # id: str | None = None
#     session_id: str
#     product_id: str
#     quantity: str
#     created_at: datetime | None = None
#     modified_at: datetime | None = None

class Cart_item(BaseModel):
    session_id: str
    product_id: str
    quantity: str

class Cart_item_in(Cart_item):
    pass

class Cart_item_outs(Cart_item):
    id: str
    created_at: datetime
    modified_at: datetime

class Cart_item_update(Cart_item):
    modified_at: datetime
    pass