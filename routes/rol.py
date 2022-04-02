#Archivo para rutas USER
#Este modulo permite definir subrutas o rutas por separado, response es para respuestas HTTP
from fastapi import APIRouter, Response, status
#Esto solo me dice a donde conectarme, no hay un schema
from config.db import conn
#Aquí traemos el schema
from models.rols import rols
#Llamada al schema usuario para crear uno
from schemas.rol import Rol, Rol_outs, Rol_in
#Modulo para generar una función de cifrado
from cryptography.fernet import Fernet
#Ahora para scar los codigos HTTP
from starlette.status import HTTP_204_NO_CONTENT

rol = APIRouter()

#Obtiene todos los roles
@rol.get("/rols", response_model=list[Rol_outs], tags=["rols"])
def get_rols():
    return conn.execute(rols.select()).fetchall()

#Obtiene un rol por id
@rol.get("/rols/{id}", response_model=Rol_outs, tags=["rols"])
def get_rol(id: str):
    return conn.execute(rols.select().where(rols.c.id == id)).first()


#Creación de un rol
@rol.post("/rols", response_model=Rol_outs, tags=["rols"])
def create_rol(rol: Rol_in):
    new_rol = {
        "name": rol.name,
        "description": rol.description
    }
    result = conn.execute(rols.insert().values(new_rol))
    return conn.execute(rols.select().where(rols.c.id == result.lastrowid)).first()

#Eliminación de un rol
@rol.delete("/rols/{id}", status_code = status.HTTP_204_NO_CONTENT, tags = ["rols"])
def delete_rol(id: str):
    conn.execute(rols.delete().where(rols.c.id == id))
    return Response(status_code = HTTP_204_NO_CONTENT)

#Actualización de un rol
@rol.put("/rols/{id}", response_model=Rol_outs, tags = ["rols"])
def update_rol(id: str, rol: Rol_in):
    conn.execute(rols.update().values(
        name = rol.name,
        description = rol.description
    ).where(rols.c.id == id))
    return conn.execute(rols.select().where(rols.c.id == id)).first()
    