from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float, Date, DateTime
from config.db import meta, engine
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.sql import func


#Creamos la tabla order_items
order_items = Table("order_items", meta,
    Column("id", Integer, primary_key=True),
    Column("order_id", Integer),
    # Column("order_id", Integer, ForeignKey("order_details.id")),
    Column("product_id", Integer),
    # Column("product_id", Integer, ForeignKey("products.id")),
    Column("quantity", Integer)
)

meta.create_all(engine)