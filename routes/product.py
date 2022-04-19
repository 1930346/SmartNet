#Archivo para rutas USER
#Este modulo permite definir subrutas o rutas por separado, response es para respuestas HTTP
import datetime
from sqlalchemy.sql import func
from fastapi import APIRouter, Response, status
#Esto solo me dice a donde conectarme, no hay un schema
from config.db import conn
#Aquí traemos el schema
from models.products import products
#Llamada al schema usuario para crear uno
from schemas.product import Product, Product_outs, Product_update, Product_in
#Modulo para generar una función de cifrado
from cryptography.fernet import Fernet
#Ahora para scar los codigos HTTP
from starlette.status import HTTP_204_NO_CONTENT

product = APIRouter()

"""
    Endpoint para obtener todos los products
    @return: lista de products
"""
#Obtiene todos los products
@product.get("/products", response_model=list[Product_outs], tags=["products"])
def get_products():
    return conn.execute(products.select()).fetchall()


"""
    Endpoint para obtener un product a través de un ID
    @param: id_product: id del product
    @return: un product
"""
#Obtiene un product por id
@product.get("/products/{id}", response_model=Product_outs, tags=["products"])
def get_product(id: str):
    return conn.execute(products.select().where(products.c.id == id)).first()

"""
    Endpoint para crear un product
    @param: product: información del product
    @return: un product
"""
#Creación de un product
@product.post("/products", response_model=Product_outs, tags=["products"])
def create_product(product: Product_in):
    new_product = {
        "name": product.name,
        "description": product.description,
        "image": product.image,
        "category_id": product.category_id,
        "price": product.price,
        "status": product.status,
        "stock": product.stock,
    }
    result = conn.execute(products.insert().values(new_product))
    return conn.execute(products.select().where(products.c.id == result.lastrowid)).first()

"""
    Endpoint para borrar un product
    @param: product: información del product
    @return: HTTP_204_NO_CONTENT
"""
#Eliminación de un product
@product.delete("/products/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["products"])
def delete_product(id: str):
    conn.execute(products.delete().where(products.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


"""
    Endpoint para actualizar un product
    @param: product: información del product
    @return: un product
"""
#Actualización de un product
@product.put("/products/{id}", response_model=Product_outs, tags=["products"])
def update_product(id: str, product: Product_update):
    conn.execute(products.update().values(
        name=product.name,
        description=product.description,
        image=product.image,
        category_id=product.category_id,
        price=product.price,
        status=product.status,
        stock = product.stock,
        modified_at = func.now() ##ask about this
    ).where(products.c.id == id))
    return conn.execute(products.select().where(products.c.id == id)).first()