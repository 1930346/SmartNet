from pydantic import BaseModel

class Product(BaseModel):
    id: str | None = None
    name: str
    description: str 
    image: str | None = None
    category_id: str
    price: float
    status: str
    created_at: str | None = None
    modified_at: str | None = None