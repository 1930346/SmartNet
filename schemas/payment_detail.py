from pydantic import BaseModel, Field

# Modelo base
# class Payment_detail(BaseModel):
#     # id: str | None = None
#     order_id: str
#     provider: str
#     amount: float

"""
    Define the Schema for the table payment_detail to use like a json object
    This class inherits from BaseModel and it defines the fields of the table
    Attributes:
        provider: indicates the provider of the payment_detail
        amount: indicates the amount of the payment_detail
"""
class Payment_detail(BaseModel):
    # order_id: str = Field(title="The id of the order")
    provider: str = Field(title="The provider of the payment")
    amount: float = Field(title="The amount of the payment")

"""
    Define the Schema for the table payment_detail to use like a json object
    This class use the BaseModel to inherit the fields of the table
    And also represents an output of the model
    Attributes:
        id: indicates the id of the payment_detail
"""
class Payment_detail_outs(Payment_detail):
    id: str = Field(title="The id of the payment")

"""
    Define the Schema for the table payment_detail to use like a json object
    This class use the BaseModel to inherit the fields of the table
    And also represents an instance of the model
"""
class Payment_detail_in(Payment_detail):
    pass

"""
    Define the Schema for the table payment_detail to use like a json object
    This class use the BaseModel to inherit the fields of the table
    And also represents an update of the model
"""
class Payment_detail_update(Payment_detail):
    pass