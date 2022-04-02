from pydantic import BaseModel, Field
from sqlalchemy.sql import func
from datetime import datetime

class Product_category(BaseModel):
    # id: str | None = None
    name: str
    description: str
    # created_at: datetime | None = None
    # modified_at: datetime | None = None

#This is a pydantic model to return data from the database
class Products_category_outs(BaseModel):
    # id: str
    name: str
    description: str
    created_at: datetime
    modified_at: datetime