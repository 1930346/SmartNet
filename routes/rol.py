#Archivo para rutas USER
#Este modulo permite definir subrutas o rutas por separado, response es para respuestas HTTP
from fastapi import APIRouter, Response, status
#Esto solo me dice a donde conectarme, no hay un schema
from config.db import conn
#Aquí traemos el schema
from models.rols import rols
#Llamada al schema usuario para crear uno
from schemas.rol import Rol
#Modulo para generar una función de cifrado
from cryptography.fernet import Fernet
#Ahora para scar los codigos HTTP
from starlette.status import HTTP_204_NO_CONTENT

rol = APIRouter()


@rol.get("/rols", response_model=list[Rol], tags=["rols"])
def get_rols():
    return conn.execute(rols.select()).fetchall()