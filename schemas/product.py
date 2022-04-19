
from pydantic import BaseModel, Field
from datetime import datetime
from sqlalchemy import values
from sqlalchemy.sql import func

# Base model
# class Product(BaseModel):
#     # id: str | None = None
#     name: str
#     description: str 
#     image: str | None = None
#     category_id: str
#     price: float
#     status: str | None = "active"
#     created_at: datetime | None = None
#     modified_at: datetime | None =  None

"""
    Define the Schema for the table product to use like a json object
    This class inherits from BaseModel and it defines the fields of the table
    Attributes:
        name: indicates the name of the product
        description: indicates the description of the product
        image: indicates the image of the product
        category_id: indicates the id of the category of the product
        price: indicates the price of the product
        status: indicates the status of the product
        stock: indicates the stock of the product
"""
class Product(BaseModel):
    name: str = Field(title = "The name of the product")
    description: str | None = Field(None, title="The description of the Product", max_length=255)
    image: str | None = Field(None, title="The image of the Product")
    category_id: str = Field(title="The category of the Product", ForeignKey = ("product_categories.id"))
    price: float = Field(title="The price of the Product" )
    status: str | None = Field("active", title = "The status of the Product" )#None = "active" 
    stock: int = Field(title="The stock of the Product")

"""
    Define the Schema for the table product to use like a json object
    This class use the BaseModel to inherit the fields of the table
    And also represents an instance of the model
"""
class Product_in(Product):
    pass

"""
    Define the Schema for the table product to use like a json object
    This class use the BaseModel to inherit the fields of the table
    And also represents an output of the model
"""
class Product_outs(Product):
    id: str = Field(title="The id of the Product")
    created_at: datetime = Field(title="The date of creation of the Product")
    modified_at: datetime = Field(title="The date of modification of the Product")

"""
    Define the Schema for the table product to use like a json object
    This class use the BaseModel to inherit the fields of the table
    And also represents an update of the model
"""
class Product_update(Product):
    # modified_at: datetime = Field(title="The date of modification of the Product")
    pass