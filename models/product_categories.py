from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float, Date, DateTime
from config.db import meta, engine
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.sql import func

"""
    Define the model for the table of products_categories in the database
    Column: indicates info about the column like type, length, ForeignKey, and default values, etc.
    Fields:
        id: indicates the id of the category
        name: indicates the name of the category
        description: indicates the description of the category
        created_at: indicates the date when the category was created
        modified_at: indicates the date when the category was modified
"""

#Creamos la tabla product_categories
product_categories = Table("product_categories", meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("description", String(255)),
    Column("created_at", DateTime, server_default = func.now()),
    Column("modified_at", DateTime, server_default = func.now())
)   

# meta.create_all(engine)