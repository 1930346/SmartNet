from pydantic import BaseModel, Field

# Modelo base
# class Order_item(BaseModel):
#     # id: str | None = None
#     order_id: str
#     product_id: str
#     quantity: str

"""
    Define the Schema for the table order_item to use like a json object
    This class inherits from BaseModel and it defines the fields of the table
    Attributes:
        order_id: indicates the id of the order that owns the order_item
        product_id: indicates the id of the product of the order_item
        quantity: indicates the quantity of the order_item
"""

class Order_item(BaseModel):
    order_id: str = Field(title="The id of the order")
    product_id: str = Field(title="The id of the product")
    quantity: str = Field(title="The quantity of the product")



"""
    Define the Schema for the table order_item to use like a json object
    This class use the BaseModel to inherit the fields of the table
    And also represents an output of the model
    Attributes:
        id: indicates the id of the order_item
"""
class Order_item_outs(Order_item):
    id: str = Field(title="The id of the order item")


"""
    Define the Schema for the table order_item to use like a json object
    This class use the BaseModel to inherit the fields of the table
    And also represents an instance of the model
"""
class Order_item_in(Order_item):
    pass

"""
    Define the Schema for the table order_item to use like a json object
    This class use the BaseModel to inherit the fields of the table
    And also represents an update of the model
"""
class Order_item_update(Order_item):
    pass