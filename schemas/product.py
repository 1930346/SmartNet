from pydantic import BaseModel
from datetime import datetime
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

class Product(BaseModel):
    name: str
    description: str
    image: str | None = None
    category_id: str    
    price: float
    status: str | None = "active"
    stock = int

class Product_in(Product):
    pass

class Product_outs(Product):
    id: str
    created_at: datetime
    modified_at: datetime

class Product_update(Product):
    modified_at: datetime
    pass