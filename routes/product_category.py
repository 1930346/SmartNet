#Archivo para rutas USER
#Este modulo permite definir subrutas o rutas por separado, response es para respuestas HTTP
import datetime
from sqlalchemy.sql import func
from fastapi import APIRouter, Response, status
#Esto solo me dice a donde conectarme, no hay un schema
from config.db import conn
#Aquí traemos el schema
from models.product_categories import product_categories
#Llamada al schema usuario para crear uno
from schemas.product_category import Product_category, Product_category_outs, Product_category_update, Product_category_in
#Modulo para generar una función de cifrado
from cryptography.fernet import Fernet
#Ahora para scar los codigos HTTP
from starlette.status import HTTP_204_NO_CONTENT

product_category = APIRouter()

"""
    Endpoint para obtener todos los product_categories
    @return: lista de product_categories
"""
#Obtiene todos los product_categories
@product_category.get("/product_categories", response_model=list[Product_category_outs], tags=["product_categories"])
def get_product_categories():
    return conn.execute(product_categories.select()).fetchall()

"""
    Endpoint para obtener un product_category a través de un ID
    @param: id_product_category: id del product_category
    @return: un product_category
"""
#Obtiene un product_category por id
@product_category.get("/product_categories/{id}", response_model=Product_category_outs, tags=["product_categories"])
def get_product_category(id: str):
    return conn.execute(product_categories.select().where(product_categories.c.id == id)).first()

"""
    Endpoint para crear un product_category
    @param: product_category: información del product_category
    @return: un product_category
"""
#Creación de un product_category
@product_category.post("/product_categories", response_model=Product_category_outs, tags=["product_categories"])
def create_product_category(product_category: Product_category_in):
    new_product_category = {
        "name": product_category.name,
        "description": product_category.description
    }
    result = conn.execute(product_categories.insert().values(new_product_category))
    return conn.execute(product_categories.select().where(product_categories.c.id == result.lastrowid)).first()

"""
    Endpoint para borrar un product_category
    @param: product_category: información del product_category
    @return: HTTP_204_NO_CONTENT
"""
#Eliminación de un product_category
@product_category.delete("/product_categories/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["product_categories"])
def delete_product_category(id: str):
    conn.execute(product_categories.delete().where(product_categories.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)

"""
    Endpoint para actualizar un product_category
    @param: product_category: información del product_category
    @return: un product_category
"""
#Actualización de un product_category
@product_category.put("/product_categories/{id}", response_model=Product_category_outs, tags=["product_categories"])
def update_product_category(id: str, product_category: Product_category_update):
    conn.execute(product_categories.update().values(
        name=product_category.name,
        description=product_category.description,
        modified_at= func.now()  #ask for this
    ).where(product_categories.c.id == id))
    return conn.execute(product_categories.select().where(product_categories.c.id == id)).first()

