#Archivo para rutas USER
#Este modulo permite definir subrutas o rutas por separado, response es para respuestas HTTP
import datetime
from sqlalchemy.sql import func
from fastapi import APIRouter, Response, status
#Esto solo me dice a donde conectarme, no hay un schema
from config.db import conn
#Aquí traemos el schema
from models.shopping_sessions import shopping_sessions
#Llamada al schema usuario para crear uno
from schemas.shopping_session import Shopping_session, Shopping_session_in, Shopping_session_outs, Shopping_session_outs, Shopping_session_update
#Modulo para generar una función de cifrado
from cryptography.fernet import Fernet
#Ahora para scar los codigos HTTP
from starlette.status import HTTP_204_NO_CONTENT

shopping_session = APIRouter()

"""
    Endpoint para obtener todos los shopping_sessions
    @return: lista de shopping_sessions
"""
#Obtiene todos los shopping_sessions
@shopping_session.get("/shopping_sessions", response_model=list[Shopping_session_outs], tags=["shopping_sessions"])
def get_shopping_sessions():
    return conn.execute(shopping_sessions.select()).fetchall()

"""
    Endpoint para obtener un shopping_session a través de un ID
    @param: id_shopping_session: id del shopping_session
    @return: un shopping_session
"""
#Obtiene un shopping_session por id
@shopping_session.get("/shopping_sessions/{id}", response_model=Shopping_session_outs, tags=["shopping_sessions"])
def get_shopping_session(id: str):
    return conn.execute(shopping_sessions.select().where(shopping_sessions.c.id == id)).first()

"""
    Endpoint para crear un shopping_session
    @param: shopping_session: información del shopping_session
    @return: un shopping_session
"""
#Creación de un shopping_session
@shopping_session.post("/shopping_sessions", response_model=Shopping_session_outs, tags=["shopping_sessions"])
def create_shopping_session(shopping_session: Shopping_session_in):
    new_shopping_session = {
        "user_id": shopping_session.user_id,
        "total": shopping_session.total,
    }
    result = conn.execute(shopping_sessions.insert().values(new_shopping_session))
    return conn.execute(shopping_sessions.select().where(shopping_sessions.c.id == result.lastrowid)).first()

"""
    Endpoint para borrar un shopping_session
    @param: id_shopping_session: id del shopping_session
    @return: HTTP_204_NO_CONTENT
"""
#Eliminación de un shopping_session
@shopping_session.delete("/shopping_sessions/{id}", status_code = status.HTTP_204_NO_CONTENT, tags = ["shopping_sessions"])
def delete_shopping_session(id: str):
    conn.execute(shopping_sessions.delete().where(shopping_sessions.c.id == id))
    return Response(status_code = HTTP_204_NO_CONTENT)

"""
    Endpoint para actualizar un shopping_session
    @param: id_shopping_session: id del shopping_session
    @param: shopping_session: información del shopping_session
    @return: un shopping_session
"""
#Actualización de un shopping_session
@shopping_session.put("/shopping_sessions/{id}", response_model = Shopping_session_outs, tags = ["shopping_sessions"])
def update_shopping_session(id: str, shopping_session: Shopping_session_update):
    conn.execute(shopping_sessions.update().values(
        user_id = shopping_session.user_id,
        total = shopping_session.total,
        modified_at = func.now()   ##Ask abour this
    ).where(shopping_sessions.c.id == id))
    return conn.execute(shopping_sessions.select().where(shopping_sessions.c.id == id)).first()