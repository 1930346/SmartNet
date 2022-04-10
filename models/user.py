#SqlAlchemy me permite crear tablas de base de datos desde python
from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float, Date, DateTime
from config.db import meta, engine
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.sql import func

#Creas la tabla, nombre users, propiedad meta, columna
users = Table("users", meta, 
    Column("id", Integer, primary_key=True),
    Column("first_name", String(255)),
    Column("last_name", String(255)),
    # Column("address", String(255)),
    Column("telephone", String(255)),
    Column("email", String(255)),
    # Column("rol_id",  Integer),
    Column("rol_id",  Integer, ForeignKey("rols.id")),
    Column("username", String(255)),
    Column("password", String(255)),
    Column("created_at", DateTime, server_default = func.now())
) 

#Una vez tengo la tabla, hay que unirla a la conexión, o sea crearla en la bd
#Se comentó porque esto la crea en el instante y la no puede encontrar referencias foráneas
# meta.create_all(engine)


