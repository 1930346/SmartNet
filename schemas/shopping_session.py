from pydantic import BaseModel, Field
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
    user_id: str = Field(title="The id of the user")
    total: float = Field(title="The total of the order")

class Shopping_session_in(Shopping_session):
    pass

class Shopping_session_outs(Shopping_session):
    id: str = Field(title="The id of the shopping session")
    created_at: datetime = Field(title="The date of creation of the shopping session")
    modified_at: datetime = Field(title="The date of modification of the shopping session")

class Shopping_session_update(Shopping_session):
    # modified_at: datetime
    pass