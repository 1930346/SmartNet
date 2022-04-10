from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.sql import func

# Clase base, comentada para aplicar herencia
# class Shopping_session(BaseModel):
#     # id: str | None = None
#     user_id: str
#     total: float
#     created_at: datetime | None = None
#     modified_at: datetime | None = None


class Shopping_session(BaseModel):
    user_id: str
    total: float

class Shopping_session_in(Shopping_session):
    pass

class Shopping_session_outs(Shopping_session):
    id: str
    created_at: datetime
    modified_at: datetime

class Shopping_session_update(Shopping_session):
    modified_at: datetime
    pass