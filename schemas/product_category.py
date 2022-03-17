from pydantic import BaseModel


class Product_category(BaseModel):
    id: str | None = None
    name: str
    description: str
    created_at: str | None = None
    modified_at: str | None = None