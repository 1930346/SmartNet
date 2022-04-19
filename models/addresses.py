from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float, Date, DateTime
from config.db import meta, engine
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.sql import func

"""
    Define the model for the table of addresses in the database
    Column: indicates info about the column like type, length, ForeignKey, and default values, etc.  
    Fields:
        id: indicates the id of the address
        user_id: indicates the id of the user that owns the address
        street: indicates the street of the address
        int_number: indicates the number of the address
        ext_number: indicates the number of the address
        colony: indicates the colony of the address
        city: indicates the city of the address
        zip_code: indicates the zip code of the address
        created_at: indicates the date when the address was created
        modified_at: indicates the date when the address was modified

"""
addresses = Table("addresses", meta,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("street", String(255)),
    Column("int_number", String(255)),
    Column("ext_number", String(255)),
    Column("colony", String(255)),
    Column("city", String(255)),
    Column("state", String(255)),
    Column("zip_code", String(255)),
    Column("created_at", DateTime, server_default = func.now()),
    Column("modified_at", DateTime, server_default = func.now())
)