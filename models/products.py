from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float, Date, DateTime
from config.db import meta, engine
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.sql import func


"""
    Define the model for the table of products in the database
    Column: indicates info about the column like type, length, ForeignKey, and default values, etc.
    Fields:
        id: indicates the id of the product
        name: indicates the name of the product
        description: indicates the description of the product
        image: indicates the image of the product
        category_id: indicates the id of the category that the product belongs to
        price: indicates the price of the product
        stock: indicates the quantity of the product in stock
        created_at: indicates the date when the product was created
        modified_at: indicates the date when the product was modified
"""
#Creamos la tabla products
products = Table("products", meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("description", String(255)),
    Column("image", String(255)),
    Column("category_id", Integer, ForeignKey("product_categories.id")),
    Column("price", Float(6,2), server_default = "0.00", default=0.00),
    Column("status", String(255), server_default = "active", default="active"),
    Column("stock", Integer, default=0),
    Column("created_at", DateTime, server_default = func.now()),
    Column("modified_at", DateTime, server_default = func.now())
)

#default param is not working.
# meta.create_all(engine)
