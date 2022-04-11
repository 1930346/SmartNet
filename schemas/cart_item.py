from pydantic import BaseModel, Field
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
    session_id: str = Field(title="The id of the session")
    product_id: str = Field(title="The id of the product")
    quantity: str = Field(title="The quantity of the product")

class Cart_item_in(Cart_item):
    pass

class Cart_item_outs(Cart_item):
    id: str = Field(title="The id of the cart item")
    created_at: datetime = Field(title="The date of creation of the cart item")
    modified_at: datetime = Field(title="The date of modification of the cart item")

class Cart_item_update(Cart_item):
    modified_at: datetime = Field(title="The date of modification of the cart item")
    pass