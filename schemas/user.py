#Aquí se crearan los usuarios cuando se recibe data del front
#Mandera de crear tipos de datos
from pydantic import BaseModel



#Creamos esta clase para los atributos en común de ambos Schemas
class User(BaseModel):
    first_name: str
    last_name: str
    address: str
    # telephone: str
    # email: str 
    username: str


class User_two(User):
    rol_id: str | None = 1
    telephone: str
    email: str 

#De esta forma ya tenemos definidos los datos para unb usuario
class User_in(User_two):
    password: str

class User_outs(User_two):
    id: str
    # password: str
    # created_at: str

class User_update(User):
    # id: str | None = None
    # name: str
    # email: str
    # password: str
    # id: str | None = None
    pass



