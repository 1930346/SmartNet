#SqlAlchemy me permite crear tablas de base de datos desde python
from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float, Date, DateTime
from config.db import meta, engine
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.sql import func


"""
    Define the model for the table of users in the database
    Column: indicates info about the column like type, length, ForeignKey, and default values, etc.
    Fields:
        id: indicates the id of the user
        first_name: indicates the first name of the user
        last_name: indicates the last name of the user
        telephone: indicates the telephone of the user
        email: indicates the email of the user
        rol_id: indicates the id of the rol of the user
        username: indicates the username of the user
        password: indicates the password of the user
        created_at: indicates the date when the user was created
"""

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


