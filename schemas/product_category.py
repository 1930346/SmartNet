from pydantic import BaseModel, Field
from sqlalchemy.sql import func


class Product_category(BaseModel):
    id: str | None = None
    name: str
    description: str
    # created_at: str | None = Field(None, example=func.sysdate())
    # modified_at: str | None = Field(None, example=func.sysdate())