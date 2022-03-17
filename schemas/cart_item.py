from pydantic import BaseModel


class Cart_item(BaseModel):
    id: str | None = None
    session_id: str
    product_id: str
    quantity: str
    created_at: str | None = None
    modified_at: str | None = None