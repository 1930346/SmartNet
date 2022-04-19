from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float, Date, DateTime
from config.db import meta, engine
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.sql import func

"""
    Define the model for the table of shopping_sessions in the database
    Column: indicates info about the column like type, length, ForeignKey, and default values, etc.
    Fields:
        id: indicates the id of the shopping_session
        user_id: indicates the id of the user that owns the shopping_session
        total: indicates the total of the shopping_session
        created_at: indicates the date when the shopping_session was created
        modified_at: indicates the date when the shopping_session was modified

"""

shopping_sessions = Table("shopping_sessions", meta,
    Column("id", Integer, primary_key=True),
    # Column("user_id", Integer),
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("total", Float, server_default = "0.00", default=0.00),
    Column("created_at", DateTime, server_default = func.now()),
    Column("modified_at", DateTime, server_default = func.now())
)

