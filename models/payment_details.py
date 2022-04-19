from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float, Date, DateTime
from config.db import meta, engine
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.sql import func

"""
    Define the model for the table of payment_details in the database
    Column: indicates info about the column like type, length, ForeignKey, and default values, etc.
    Fields:
        id: indicates the id of the payment_detail
        provider: indicates the payment provider
        amount: indicates the amount to pay
"""

payment_details = Table("payment_details", meta,
    Column("id", Integer, primary_key=True),
    # Column("order_id", Integer),
    # Column("order_id", Integer, ForeignKey("order_details.id")),
    Column("provider", String(255)),
    Column("amount", Float, default = 0.00)
)

# meta.create_all(engine)