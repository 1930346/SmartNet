from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float, Date, DateTime
from config.db import meta, engine
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.sql import func


#Creamos la tabla rols
rols = Table("rols", meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("description", String(255))
)

meta.create_all(engine)