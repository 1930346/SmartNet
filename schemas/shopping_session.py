from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.sql import func

class Shopping_session(BaseModel):
    # id: str | None = None
    user_id: str
    total: float
    created_at: datetime | None = None
    modified_at: datetime | None = None