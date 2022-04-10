#Aquí se crearan los usuarios cuando se recibe data del front
#Mandera de crear tipos de datos
from datetime import datetime
from pydantic import BaseModel

#Creamos esta clase para los atributos en común de ambos Schemas
class User(BaseModel):
    first_name: str
    last_name: str
    username: str

class User_two(User):
    rol_id: str | None = 1
    telephone: str
    email: str 

#De esta forma ya tenemos definidos los datos para un usuario
class User_in(User_two):
    password: str

#Literal sólo para gets
class User_outs(User_two):
    id: str
    created_at: datetime

#No podemos actualizar dirección y teléfono por motivos de seguridad
class User_update(User):
    pass



