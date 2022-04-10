#Archivo para rutas USER
#Este modulo permite definir subrutas o rutas por separado, response es para respuestas HTTP
from fastapi import APIRouter, Response, status
#Esto solo me dice a donde conectarme, no hay un schema
from config.db import conn
#Aquí traemos el schema
from models.order_details import order_details
#Llamada al schema usuario para crear uno
from schemas.order_detail import Order_detail, Order_detail_in, Order_detail_out, Order_detail_outs, Order_detail_update
#Modulo para generar una función de cifrado
from cryptography.fernet import Fernet
#Ahora para scar los codigos HTTP
from starlette.status import HTTP_204_NO_CONTENT

order_detail = APIRouter()


#Obtiene todos los order_details
@order_detail.get("/order_details", response_model=list[Order_detail_outs], tags=["order_details"])
def get_order_details():
    return conn.execute(order_details.select()).fetchall()

#Obtiene un order_detail por id
@order_detail.get("/order_details/{id}", response_model=Order_detail_outs, tags=["order_details"])
def get_order_detail(id: str):
    return conn.execute(order_details.select().where(order_details.c.id == id)).first()


#Creación de un order_detail
@order_detail.post("/order_details", response_model=Order_detail_outs, tags=["order_details"])
def create_order_detail(order_detail: Order_detail_in):
    new_order_detail = {
        "user_id": order_detail.user_id,
        "payment_id": order_detail.payment_id,
        "total": order_detail.total,
        #"created_at": order_detail.created_at,
    }
    result = conn.execute(order_details.insert().values(new_order_detail))
    return conn.execute(order_details.select().where(order_details.c.id == result.lastrowid)).first()


#Eliminación de un order_detail
@order_detail.delete("/order_details/{id}", status_code = status.HTTP_204_NO_CONTENT, tags = ["order_details"])
def delete_order_detail(id: str):
    conn.execute(order_details.delete().where(order_details.c.id == id))
    return Response(status_code = HTTP_204_NO_CONTENT)

#Actualización de un order_detail
@order_detail.put("/order_details/{id}", response_model=Order_detail_outs, tags = ["order_details"])
def update_order_detail(id: str, order_detail: Order_detail_update):
    conn.execute(order_details.update().values(
        user_id = order_detail.user_id,
        payment_id = order_detail.payment_id,
        total = order_detail.total,
        #created_at = order_detail.created_at,
    ).where(order_details.c.id == id))
    return conn.execute(order_details.select().where(order_details.c.id == id)).first()