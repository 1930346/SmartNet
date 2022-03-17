from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float, Date, DateTime
from config.db import meta, engine
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.sql import func


order_details = Table("order_details", meta,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer),
    # Column("user_id", Integer, ForeignKey("users.id")),
    Column("payment_id", Integer),
    # Column("payment_id", Integer, ForeignKey("payment_details.id")),
    Column("total", Float, default=0.00),
    Column("created_at", DateTime, server_default = func.sysdate())
)

meta.create_all(engine)