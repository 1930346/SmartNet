from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float, Date, DateTime
from config.db import meta, engine
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.sql import func

"""
    Define the model for the table of order_items in the database
    Column: indicates info about the column like type, length, ForeignKey, and default values, etc.
    Fields:
        id: indicates the id of the order_item
        order_id: indicates the id of the order that owns the order_item
        product_id: indicates the id of the product that is in the order_item
        quantity: indicates the quantity of the product in the order_item
"""

#Creamos la tabla order_items
order_items = Table("order_items", meta,
    Column("id", Integer, primary_key=True),
    # Column("order_id", Integer),
    Column("order_id", Integer, ForeignKey("order_details.id")),
    # Column("product_id", Integer),
    Column("product_id", Integer, ForeignKey("products.id")),
    Column("quantity", Integer)
)

# meta.create_all(engine)