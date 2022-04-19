from pydantic import BaseModel, Field
from sqlalchemy.sql import func
from datetime import datetime

# Modelo base
# class Product_category(BaseModel):
#     # id: str | None = None
#     name: str
#     description: str
#     created_at: datetime | None = None
#     modified_at: datetime | None = None

"""
    Define the Schema for the table product_category to use like a json object
    This class inherits from BaseModel and it defines the fields of the table
    Attributes:
        name: indicates the name of the product_category
        description: indicates the description of the product_category
"""
class Product_category(BaseModel):
    name: str = Field(title = "The name of the product category")
    description: str = Field(title="The description of the product category")


"""
    Define the Schema for the table product_category to use like a json object
    This class use the BaseModel to inherit the fields of the table
    And also represents an output of the model
    Attributes:
        id: indicates the id of the product_category
        created_at: indicates the date of the product_category creation
        modified_at: indicates the date of the product_category modification
"""    
#This is a pydantic model to return data from the database
class Product_category_outs(BaseModel):
    id: str = Field(title="The id of the product category")
    created_at: datetime = Field(title="The date of creation of the product category")
    modified_at: datetime = Field(title="The date of modification of the product category")

"""
    Define the Schema for the table product_category to use like a json object
    This class use the BaseModel to inherit the fields of the table
    And also represents an input of the model
"""
class Product_category_in(Product_category):
    pass

"""
    Define the Schema for the table product_category to use like a json object
    This class use the BaseModel to inherit the fields of the table
    And also represents an update of the model
"""
class Product_category_update(Product_category):
    # modified_at: datetime = Field(title="The date of modification of the product category")
    pass