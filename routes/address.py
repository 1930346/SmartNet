#Archivo para rutas USER
#Este modulo permite definir subrutas o rutas por separado, response es para respuestas HTTP
import datetime
from sqlalchemy.sql import func
from fastapi import APIRouter, Response, status
#Esto solo me dice a donde conectarme, no hay un schema
from config.db import conn
#Aquí traemos el schema
from models.addresses import addresses
#Llamada al schema usuario para crear uno
from schemas.address import Address, Address_in, Address_outs, Address_update
#Modulo para generar una función de cifrado
from cryptography.fernet import Fernet
#Ahora para scar los codigos HTTP
from starlette.status import HTTP_204_NO_CONTENT


address = APIRouter()


#Obtiene todas las direcciones
@address.get("/addresses", response_model=list[Address_outs], tags=["addresses"])
def get_addresses():
    return conn.execute(addresses.select()).fetchall()

#Obtiene una dirección por id
@address.get("/addresses/{id}", response_model=Address_outs, tags=["addresses"])
def get_address(id: str):
    return conn.execute(addresses.select().where(addresses.c.id == id)).first()

#Crea una dirección
@address.post("/addresses", response_model=Address_outs, tags=["addresses"])   
def create_address(address: Address_in):
    new_address = {
        "user_id": address.user_id,
        "street": address.street,
        "int_number": address.int_number,
        "ext_number": address.ext_number,
        "colony": address.colony,
        "city": address.city,
        "state": address.state,
        "zip_code": address.zip_code,
    }
    result = conn.execute(addresses.insert().values(new_address))
    return conn.execute(addresses.select().where(addresses.c.id == result.lastrowid)).first()

#Elimina una dirección
@address.delete("/addresses/{id}", status_code = status.HTTP_204_NO_CONTENT, tags = ["addresses"])
def delete_address(id: str):
    conn.execute(addresses.delete().where(addresses.c.id == id))
    return Response(status_code = HTTP_204_NO_CONTENT)

#Actualiza una dirección
@address.put("/addresses/{id}", response_model=Address_outs, tags = ["addresses"])
def update_address(id: str, address: Address_update):
    conn.execute(addresses.update().values(
        street = address.street,
        int_number = address.int_number,
        ext_number = address.ext_number,
        colony = address.colony,
        city = address.city,
        state = address.state,
        zip_code = address.zip_code,
        modified_at = func.now()
        
    ).where(addresses.c.id == id))
    return conn.execute(addresses.select().where(addresses.c.id == id)).first()
