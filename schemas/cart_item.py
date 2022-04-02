from pydantic import BaseModel
from datetime import datetime


class Cart_item(BaseModel):
    # id: str | None = None
    session_id: str
    product_id: str
    quantity: str
    created_at: datetime | None = None
    modified_at: datetime | None = None