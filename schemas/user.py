#Aquí se crearan los usuarios cuando se recibe data del front
#Mandera de crear tipos de datos
from pydantic import BaseModel

#De esta forma ya tenemos definidos los datos para unb usuario
class User(BaseModel):
    #Esto se hace para no importal optional, ya que hace el atributo opcional
    # id: str | None = None
    # name: str
    # email: str
    # password: str

    id: str | None = None
    first_name: str
    last_name: str
    address: str
    telephone: str
    email: str
    rol_id: str
    username: str
    password: str

