from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float, Date, DateTime
from config.db import meta, engine
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.sql import func

"""
    Define the model for the table of cart_items in the database
    Column: indicates info about the column like type, length, ForeignKey, and default values, etc.
    Fields:
        id: indicates the id of the cart_item
        session_id: indicates the id of the shopping_session that owns the cart_item
        product_id: indicates the id of the product that is in the cart_item
        quantity: indicates the quantity of the product in the cart_item
        created_at: indicates the date when the cart_item was created
        modified_at: indicates the date when the cart_item was modified
"""

#Creamos la tabla cart_items    
cart_items = Table("cart_items", meta,
    Column("id", Integer, primary_key=True),
    # Column("session_id", Integer),
    Column("session_id", Integer, ForeignKey("shopping_sessions.id")),
    # Column("product_id", Integer),
    Column("product_id", Integer, ForeignKey("products.id")),
    Column("quantity", Integer),
    Column("created_at", DateTime, server_default = func.now()),
    Column("modified_at", DateTime, server_default = func.now())
)

# meta.create_all(engine)