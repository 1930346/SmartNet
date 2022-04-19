from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float, Date, DateTime
from config.db import meta, engine
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.sql import func

"""
    Define the model for the table of order_details in the database
    Column: indicates info about the column like type, length, ForeignKey, and default values, etc.
    Fields:
        id: indicates the id of the order_detail
        user_id: indicates the id of the user that owns the order_detail
        payment_id: indicates the id of the payment that is associated with the order_detail
        total: indicates the total of the order_detail
        created_at: indicates the date when the order_detail was created
"""
order_details = Table("order_details", meta,
    Column("id", Integer, primary_key=True),
    # Column("user_id", Integer),
    Column("user_id", Integer, ForeignKey("users.id")),
    # Column("payment_id", Integer),
    Column("payment_id", Integer, ForeignKey("payment_details.id")),
    Column("total", Float, default=0.00),
    Column("created_at", DateTime, server_default = func.now())
)

# meta.create_all(engine)