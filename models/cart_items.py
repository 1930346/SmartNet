from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float, Date, DateTime
from config.db import meta, engine
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.sql import func


#Creamos la tabla cart_items    
cart_items = Table("cart_items", meta,
    Column("id", Integer, primary_key=True),
    # Column("session_id", Integer),
    Column("session_id", Integer, ForeignKey("shopping_sessions.id")),
    # Column("product_id", Integer),
    Column("product_id", Integer, ForeignKey("products.id")),
    Column("quantity", Integer),
    Column("created_at", DateTime, server_default = func.sysdate()),
    Column("modified_at", DateTime, server_default = func.sysdate())
)

# meta.create_all(engine)