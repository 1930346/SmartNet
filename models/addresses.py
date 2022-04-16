from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float, Date, DateTime
from config.db import meta, engine
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.sql import func


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