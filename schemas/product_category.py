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
    name: str
    description: str

    
#This is a pydantic model to return data from the database
class Product_category_outs(BaseModel):
    id: str
    created_at: datetime
    modified_at: datetime

class Product_category_in(Product_category):
    pass

class Product_category_update(Product_category):
    modified_at: datetime
    pass