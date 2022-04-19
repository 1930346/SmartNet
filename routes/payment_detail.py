#Archivo para rutas USER
#Este modulo permite definir subrutas o rutas por separado, response es para respuestas HTTP
from fastapi import APIRouter, Response, status
#Esto solo me dice a donde conectarme, no hay un schema
from config.db import conn
#Aquí traemos el schema
from models.payment_details import payment_details
#Llamada al schema usuario para crear uno
from schemas.payment_detail import Payment_detail, Payment_detail_in, Payment_detail_outs, Payment_detail_update
#Modulo para generar una función de cifrado
from cryptography.fernet import Fernet
#Ahora para scar los codigos HTTP
from starlette.status import HTTP_204_NO_CONTENT

payment_detail = APIRouter()


"""
    Endpoint para obtener todos los payment_details
    @return: lista de payment_details
"""
#Obtiene todos los payment_details
@payment_detail.get("/payment_details", response_model=list[Payment_detail_outs], tags=["payment_details"])
def get_payment_details():
    return conn.execute(payment_details.select()).fetchall()

"""
    Endpoint para obtener un payment_detail a través de un ID
    @param: id_payment_detail: id del payment_detail
"""
#Obtiene un payment_detail por id
@payment_detail.get("/payment_details/{id}", response_model=Payment_detail_outs, tags=["payment_details"])
def get_payment_detail(id: str):
    return conn.execute(payment_details.select().where(payment_details.c.id == id)).first()

"""
    Endpoint para crear un payment_detail
    @param: payment_detail: información del payment_detail
    @return: un payment_detail
"""
#Creación de un payment_detail
@payment_detail.post("/payment_details", response_model=Payment_detail_outs, tags=["payment_details"])
def create_payment_detail(payment_detail: Payment_detail_in):
    new_payment_detail = {
        # "order_id": payment_detail.order_id,
        "provider": payment_detail.provider,
        "amount": payment_detail.amount,
    }
    result = conn.execute(payment_details.insert().values(new_payment_detail))
    return conn.execute(payment_details.select().where(payment_details.c.id == result.lastrowid)).first()

"""
    Endpoint para borrar un payment_detail
    @param: payment_detail: información del payment_detail
    @return:  HTTP_204_NO_CONTENT
"""
#Eliminación de un payment_detail
@payment_detail.delete("/payment_details/{id}", status_code = status.HTTP_204_NO_CONTENT, tags = ["payment_details"])
def delete_payment_detail(id: str):
    conn.execute(payment_details.delete().where(payment_details.c.id == id))
    return Response(status_code = HTTP_204_NO_CONTENT)

"""
    Endpoint para actualizar un payment_detail
    @param: payment_detail: información del payment_detail
    @return: un payment_detail
"""
#Actualización de un payment_detail
@payment_detail.put("/payment_details/{id}", response_model = Payment_detail_outs, tags = ["payment_details"])
def update_payment_detail(id: str, payment_detail: Payment_detail_update):
    conn.execute(payment_details.update().values(
        # order_id = payment_detail.order_id,
        provider = payment_detail.provider,
        amount = payment_detail.amount,
    ).where(payment_details.c.id == id))
    return conn.execute(payment_details.select().where(payment_details.c.id == id)).first()


