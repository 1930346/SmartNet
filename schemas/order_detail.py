from pydantic import BaseModel, Field
from datetime import datetime

# Modelo base
# class Order_detail(BaseModel):
#     # id: str | None = None
#     user_id: str 
#     payment_id: str
#     total: float
#     # created_at: datetime | None = None

"""
    Define the Schema for the table order_detail to use like a json object
    This class inherits from BaseModel and it defines the fields of the table
    Attributes:
        user_id: indicates the id of the user that owns the order_detail
        payment_id: indicates the id of the payment of the order_detail
        total: indicates the total of the order_detail
"""
class Order_detail(BaseModel):
    user_id: str = Field(title="The id of the user")
    payment_id: str = Field(title="The id of the payment")
    total: float = Field(title="The total of the order")

"""
    Define the Schema for the table order_detail to use like a json object
    This class use the BaseModel to inherit the fields of the table
    And also represents an instance of the model
"""
class Order_detail_in(Order_detail):
    pass


"""
    Define the Schema for the table order_detail to use like a json object
    This class use the BaseModel to inherit the fields of the table
    And also represents an output of the model
    Attributes:
        id: indicates the id of the order_detail
        created_at: indicates the date of the order_detail creation
"""
class Order_detail_outs(Order_detail):
    id: str = Field(title="The id of the order")
    created_at: datetime = Field(title="The date of creation of the order")

"""
    Define the Schema for the table order_detail to use like a json object
    This class use the BaseModel to inherit the fields of the table
    And also represents an update of the model
"""
class Order_detail_update(Order_detail):
    pass