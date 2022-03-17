from pydantic import BaseModel


class Shopping_session(BaseModel):
    id: str | None = None
    user_id: str
    total: float
    created_at: str | None = None
    modified_at: str | None = None