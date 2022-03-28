from email.policy import default
from tkinter import N
from pydantic import BaseModel
class Product(BaseModel):
    id: str | None = None
    name: str
    description: str 
    image: str | None = None
    category_id: str
    price: float
    status: str | None = "active"
    created_at: str | None = None
    modified_at: str | None = None