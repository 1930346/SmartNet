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


"""
    Define the Schema for the table shopping_session to use like a json object
    This class inherits from BaseModel and it defines the fields of the table
    Attributes:
        user_id: indicates the id of the user that owns the shopping_session
        total: indicates the total of the shopping_session
"""
class Shopping_session(BaseModel):
    user_id: str = Field(title="The id of the user")
    total: float = Field(title="The total of the order")

"""
    Define the Schema for the table shopping_session to use like a json object
    This class use the BaseModel to inherit the fields of the table
    And also represents an instance of the model
"""
class Shopping_session_in(Shopping_session):
    pass

"""
    Define the Schema for the table shopping_session to use like a json object
    This class use the BaseModel to inherit the fields of the table
    And also represents an output of the model
    Attributes:
        id: indicates the id of the shopping_session
        created_at: indicates the date of the shopping_session creation
        modified_at: indicates the date of the shopping_session modification
"""
class Shopping_session_outs(Shopping_session):
    id: str = Field(title="The id of the shopping session")
    created_at: datetime = Field(title="The date of creation of the shopping session")
    modified_at: datetime = Field(title="The date of modification of the shopping session")

"""
    Define the Schema for the table shopping_session to use like a json object
    This class use the BaseModel to inherit the fields of the table
    And also represents an update of the model
"""
class Shopping_session_update(Shopping_session):
    # modified_at: datetime
    pass