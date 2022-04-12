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

class Product_category(BaseModel):
    name: str = Field(title = "The name of the product category")
    description: str = Field(title="The description of the product category")

    
#This is a pydantic model to return data from the database
class Product_category_outs(BaseModel):
    id: str = Field(title="The id of the product category")
    created_at: datetime = Field(title="The date of creation of the product category")
    modified_at: datetime = Field(title="The date of modification of the product category")

class Product_category_in(Product_category):
    pass

class Product_category_update(Product_category):
    # modified_at: datetime = Field(title="The date of modification of the product category")
    pass