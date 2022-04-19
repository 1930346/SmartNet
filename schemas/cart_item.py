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

"""
    Define the Schema for the table cart_item to use like a json object
    This class inherits from BaseModel and it defines the fields of the table
    Attributes:
        session_id: indicates the id of the session that owns the cart_item
        product_id: indicates the id of the product of the cart_item
        quantity: indicates the quantity of the cart_item
"""
class Cart_item(BaseModel):
    session_id: str = Field(title="The id of the session")
    product_id: str = Field(title="The id of the product")
    quantity: str = Field(title="The quantity of the product")

"""
    Define the Schema for the table cart_item to use like a json object
    This class use the BaseModel to inherit the fields of the table
    And also represents an instance of the model
"""
class Cart_item_in(Cart_item):
    pass

"""
    Define the Schema for the table cart_item to use like a json object
    This class use the BaseModel to inherit the fields of the table
    And also represents an output of the model
    Attributes:
        id: indicates the id of the cart_item
        created_at: indicates the date of the cart_item creation
        modified_at: indicates the date of the cart_item modification
"""
class Cart_item_outs(Cart_item):
    id: str = Field(title="The id of the cart item")
    created_at: datetime = Field(title="The date of creation of the cart item")
    modified_at: datetime = Field(title="The date of modification of the cart item")

"""
    Define the Schema for the table cart_item to use like a json object
    This class use the BaseModel to inherit the fields of the table
    And also represents an update of the model
"""
class Cart_item_update(Cart_item):
    # modified_at: datetime = Field(title="The date of modification of the cart item")
    pass