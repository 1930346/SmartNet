#Archivo para rutas USER
#Este modulo permite definir subrutas o rutas por separado, response es para respuestas HTTP
from fastapi import APIRouter, Response, status
#Esto solo me dice a donde conectarme, no hay un schema
from config.db import conn
#Aquí traemos el schema
from models.order_items import order_items
#Llamada al schema usuario para crear uno
from schemas.order_item import Order_item, Order_item_outs, Order_item_in, Order_item_update
#Modulo para generar una función de cifrado
from cryptography.fernet import Fernet
#Ahora para scar los codigos HTTP
from starlette.status import HTTP_204_NO_CONTENT


order_item = APIRouter()

"""
    Endpoint para obtener todos los order_items
    @return: lista de order_items
"""
#Obtiene todos los order_items
@order_item.get("/order_items", response_model=list[Order_item_outs], tags=["order_items"])
def get_order_items():
    return conn.execute(order_items.select()).fetchall()

"""
    Endpoint para obtener un order_item a través de un ID
    @param: id_order_item: id del order_item
"""
#Obtiene un order_item por id
@order_item.get("/order_items/{id}", response_model=Order_item_outs, tags=["order_items"])
def get_order_item(id: str):
    return conn.execute(order_items.select().where(order_items.c.id == id)).first()

"""
    Endpoint para crear un order_item
    @param: order_item: información del order_item
    @return: un order_item
"""
#Creación de un order_item
@order_item.post("/order_items", response_model=Order_item_outs, tags=["order_items"])
def create_order_item(order_item: Order_item_in):
    new_order_item = {
        "order_id": order_item.order_id,
        "product_id": order_item.product_id,
        "quantity": order_item.quantity
    }
    result = conn.execute(order_items.insert().values(new_order_item))
    return conn.execute(order_items.select().where(order_items.c.id == result.lastrowid)).first()

"""
    Endpoint para borrar un order_item
    @param: order_item: información del order_item
    @return: HTTP_204_NO_CONTENT
"""
#Eliminación de un order_item
@order_item.delete("/order_items/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["order_items"])
def delete_order_item(id: str):
    conn.execute(order_items.delete().where(order_items.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)

"""
    Endpoint para actualizar un order_item
    @param: order_item: información del order_item
    @return: un order_item
"""
#Actualización de un order_item
@order_item.put("/order_items/{id}", response_model=Order_item_outs, tags=["order_items"])
def update_order_item(id: str, order_item: Order_item_update):
    conn.execute(order_items.update().values(
        order_id = order_item.order_id,
        product_id = order_item.product_id,
        quantity = order_item.quantity
    ).where(order_items.c.id == id))
    return conn.execute(order_items.select().where(order_items.c.id == id)).first()
