from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float, Date, DateTime
from config.db import meta, engine
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.sql import func


#Creamos la tabla products
products = Table("products", meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("description", String(255)),
    Column("image", String(255)),
    Column("category_id", Integer, ForeignKey("product_categories.id")),
    Column("price", Float, default=0.00),
    Column("status", String(255), default="active"),
    Column("stock", Integer, default=0),
    Column("created_at", DateTime, server_default = func.now()),
    Column("modified_at", DateTime, server_default = func.now())
)

# meta.create_all(engine)
