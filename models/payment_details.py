from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float, Date, DateTime
from config.db import meta, engine
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.sql import func

payment_details = Table("payment_details", meta,
    Column("id", Integer, primary_key=True),
    # Column("order_id", Integer),
    Column("order_id", Integer, ForeignKey("order_details.id")),
    Column("provider", String(255)),
    Column("amount", Float)
)

# meta.create_all(engine)