from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.sql import func
class Product(BaseModel):
    # id: str | None = None
    name: str
    description: str 
    image: str | None = None
    category_id: str
    price: float
    status: str | None = "active"
    created_at: datetime | None = None
    modified_at: datetime | None =  None