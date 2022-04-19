from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float, Date, DateTime
from config.db import meta, engine
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.sql import func

"""
    Define the model for the table of rols in the database
    Column: indicates info about the column like type, length, ForeignKey, and default values, etc.
    Fields:
        id: indicates the id of the rol (1 user, 2 admin)
        name: indicates the name of the rol
        description: indicates the description of the rol
"""
#Creamos la tabla rols
rols = Table("rols", meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("description", String(255))
)

# meta.create_all(engine)