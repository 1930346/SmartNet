#Aquí se crearan los usuarios cuando se recibe data del front
#Mandera de crear tipos de datos
from datetime import datetime
from pydantic import BaseModel, Field

#Creamos esta clase para los atributos en común de ambos Schemas
class User(BaseModel):
    first_name: str = Field(title="The first name of the user")
    last_name: str = Field(title="The last name of the user")
    username: str = Field(title="The username of the user")

class User_two(User):
    rol_id: str | None = Field(1, title="The id of the rol")
    telephone: str = Field(title="The telephone of the user")
    email: str = Field(title="The email of the user")

#De esta forma ya tenemos definidos los datos para un usuario
class User_in(User_two):
    password: str = Field(title="The password of the user")

#Literal sólo para gets
class User_outs(User_two):
    id: str = Field(title="The id of the user")
    created_at: datetime = Field(title="The date of creation of the user")

#No podemos actualizar dirección y teléfono por motivos de seguridad
class User_update(User):
    pass



