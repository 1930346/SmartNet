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
from config.db import engine, meta

meta.create_all(engine)

app = FastAPI(
    title="Prueba API",
    description="API for SmartNet Store",
    openapi_tags = [{
        "name": "users",
        "description": "Operations about users (user routes)"
    },
    {
        "name": "cart_items",
        "description": "Operations about cart_items (cart_item routes)"
    },
    {
        "name": "order_details",
        "description": "Operations about order_details (order_detail routes)"
    },
    {
        "name": "order_items",
        "description": "Operations about order_items (order_item routes)"
    },
    {
        "name": "payment_details",
        "description": "Operations about payment_details (payment_detail routes)"
    },
    {
        "name": "product_categories",
        "description": "Operations about product_categories (product_category routes)"
    },
    {
        "name": "products",
        "description": "Operations about products (product routes)"
    },
    {
        "name": "rols",
        "description": "Operations about rols (rol routes)"
    },
    {
        "name": "shopping_sessions",
        "description": "Operations about shopping_sessions (shopping_session routes)"
    }
    
    
    ]
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


