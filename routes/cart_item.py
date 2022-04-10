#Archivo para rutas USER
#Este modulo permite definir subrutas o rutas por separado, response es para respuestas HTTP
import datetime
from fastapi import APIRouter, Response, status
#Esto solo me dice a donde conectarme, no hay un schema
from config.db import conn
#Aquí traemos el schema
from models.cart_items import cart_items
#Llamada al schema usuario para crear uno
from schemas.cart_item import Cart_item, Cart_item_outs, Cart_item_update, Cart_item_in
#Modulo para generar una función de cifrado
from cryptography.fernet import Fernet
#Ahora para scar los codigos HTTP
from starlette.status import HTTP_204_NO_CONTENT

cart_item = APIRouter()


#Obtenemos todos los cart_items
@cart_item.get("/cart_items", response_model=list[Cart_item_outs], tags = ["cart_items"])
def get_cart_items():
    return conn.execute(cart_item.select()).fetchall()


#Obtención de un cart_item por id
@cart_item.get("/cart_items/{id}", response_model=Cart_item_outs, tags = ["cart_items"])
def get_cart_item(id: str):
    return conn.execute(cart_item.select().where(cart_item.c.id == id)).first()


#Creación de un cart_item
@cart_item.post("/cart_items", response_model=Cart_item_outs, tags = ["cart_items"])
def create_cart_item(cart_item: Cart_item_in):
    new_cart_item = {
        "session_id": cart_item.session_id,
        "product_id": cart_item.product_id,
        "quantity": cart_item.quantity
        # "created_at": cart_item.created_at,
        # "modified_at": cart_item.modified_at
    }
    result = conn.execute(cart_item.insert().values(new_cart_item))
    return conn.execute(cart_item.select().where(cart_item.c.id == result.lastrowid)).first()

#Eliminación de un cart_item
@cart_item.delete("/cart_items/{id}", status_code = status.HTTP_204_NO_CONTENT, tags = ["cart_items"])
def delete_cart_item(id: str):
    conn.execute(cart_item.delete().where(cart_item.c.id == id))
    return Response(status_code = HTTP_204_NO_CONTENT)


#Actualización de un cart_item
@cart_item.put("/cart_items/{id}", response_model=Cart_item_outs, tags = ["cart_items"])
def update_cart_item(id: str, cart_item: Cart_item_update):
    conn.execute(cart_items.update().values(
        session_id = cart_item.session_id,
        product_id = cart_item.product_id,
        quantity = cart_item.quantity,
        # created_at = cart_item.created_at,
        modified_at = datetime.now() #ask about this
    ).where(cart_items.c.id == id))
    return conn.execute(cart_item.select().where(cart_item.c.id == id)).first()