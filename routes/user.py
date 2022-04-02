#Archivo para rutas USER
#Este modulo permite definir subrutas o rutas por separado, response es para respuestas HTTP
from fastapi import APIRouter, Response, status
#Esto solo me dice a donde conectarme, no hay un schema
from config.db import conn
#Aquí traemos el schema
from models.user import users
#Llamada al schema usuario para crear uno
from schemas.user import User, User_outs, User_in, User_update
#Modulo para generar una función de cifrado
from cryptography.fernet import Fernet
#Ahora para scar los codigos HTTP
from starlette.status import HTTP_204_NO_CONTENT


#Me permite hacer único cada cifrado
key = Fernet.generate_key()
f = Fernet(key)

#Ahorap uedo hacer esto
user = APIRouter()


#y poner esto
#Nota el response_model es para que en la docu se muestre que doy como respuesta
#Nota el tags es para categorizarlas de que pertenecen a la misma ruta users
@user.get("/users", response_model=list[User_outs], tags=["users"])
def get_users():
    #En lugar de retornar un hello world como antes,
    #retornamos una consulta, pero como usamos sqlalchemy
    #podemos retornar la conexión, el execute que recibe una consulta
    #y del modelo usuarios hacemos un select * y traer todo con el fetchall
    return conn.execute(users.select()).fetchall()
#Hasta este punto, no tenemos usuarios, pero podemos crearlos con un post


#Esta requerirá de un Schema para enviar datos., recibe datos del front 
@user.post("/users", response_model=User_outs, tags=["users"])
def create_user(user: User_in):
    #Aquí no nos da como diccionarios, nos sirve más para manipularlo mejor
    #print(user)
    # new_user = {
    #     "name": user.name, 
    #     "email": user.email}
    new_user = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "address": user.address,
        "telephone": user.telephone,
        "email": user.email,
        "rol_id": user.rol_id,
        "username": user.username,
        }
    #La separamos porque es necesario encriptarla
    #Para hacerlo hay bibliotecas de python como Cryptography
    #La encodeamos porque recibe bytes y en su código utf-8
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    #print(new_user)
    #Ahora lo mandamos a la DB
    result = conn.execute(users.insert().values(new_user))
    #Esto me imprime un cursor, que es la respuesta de la DB
    #print(result)
    #Ahora bien hay quye darle el resultado al cliente
    #Para ello retornamos el usuario que ha sido creado
    #con result.lastrowid, que es el id del usuario generado
    #print(result.lastrowid)
    #Con esto de la conexión, se ejecuta un select, pero donde 
    # el id es el del row id generado, (la c representa columna). devuelve una lista y sólo jalo el primero
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()


#Función de un único usuario
@user.get("/users/{id}", response_model=User_outs, tags=["users"])
def get_user(id: str):
    return conn.execute(users.select().where(users.c.id == id)).first()

#Función para eliminar un usuario, aquí se usa status code de status de fastapi, por la docu
@user.delete("/users/{id}", status_code = status.HTTP_204_NO_CONTENT, tags=["users"])
def delete_user(id: str):
    conn.execute(users.delete().where(users.c.id == id))
    #Normalmente aquí no se retorna un result, sino una respuesta HTTP, como 200, 404 etc.
    return Response(status_code=HTTP_204_NO_CONTENT)

#Función para actualizar un usuario
@user.put("/users/{id}", response_model = User_outs, tags=["users"])
def update_user(id: str, user: User_update):
    # conn.execute(users.update().values(
    #     name=user.name,
    #     email=user.email,
    #     password = f.encrypt(user.password.encode("utf-8"))).where(users.c.id == id))
    
    conn.execute(users.update().values(
        first_name=user.first_name,
        last_name=user.last_name,
        address=user.address,
        # telephone=user.telephone,
        # email=user.email,
        username=user.username).where(users.c.id == id))
    return conn.execute(users.select().where(users.c.id == id)).first()

