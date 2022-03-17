from fastapi import FastAPI
from routes.user import user
from routes.cart_item import cart_item
from routes.order_detail import order_detail
from routes.order_item import order_item
from routes.payment_detail import payment_detail
from routes.product_category import product_category
from routes.product import product
from routes.rol import rol
from routes.shopping_session import shopping_session



app = FastAPI(
    title="Prueba API",
    description="Este es un ejemplo de una API con FastAPI",
    openapi_tags = [{
        "name": "users",
        "description": "Operations about users (user routes)"
    }]
) 

app.include_router(user) #Mi app incluya las rutas que vienen de user
app.include_router(rol)
app.include_router(product)
app.include_router(product_category)
app.include_router(cart_item)
app.include_router(order_detail)
app.include_router(order_item)
app.include_router(payment_detail)
app.include_router(shopping_session)


