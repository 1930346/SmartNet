#Aquí se crearan los usuarios cuando se recibe data del front
#Mandera de crear tipos de datos
from datetime import datetime
from pydantic import BaseModel, Field

"""
    Define the Schema for the table user to use like a json object
    This class inherits from BaseModel and it defines the fields of the table
    Attributes:
        first_name: indicates the first name of the user
        last_name: indicates the last name of the user
        username: indicates the username of the user
"""
#Creamos esta clase para los atributos en común de ambos Schemas
class User(BaseModel):
    first_name: str = Field(title="The first name of the user")
    last_name: str = Field(title="The last name of the user")
    username: str = Field(title="The username of the user")

"""
    Define the Schema for the table user to use like a json object
    This class use the BaseModel to inherit the fields of the table
    And also represents an combination of the model
    Attributes:
        rol_id: indicates the id of the role of the user
        telephone: indicates the telephone of the user
        email: indicates the email of the user
"""
class User_two(User):
    rol_id: str | None = Field(1, title="The id of the rol")
    telephone: str = Field(title="The telephone of the user")
    email: str = Field(title="The email of the user")

"""
    Define the Schema for the table user to use like a json object
    This class use the BaseModel to inherit the fields of the table
    And also represents an instance of the model
    Attributes:
        password: indicates the password of the user
"""
#De esta forma ya tenemos definidos los datos para un usuario
class User_in(User_two):
    password: str = Field(title="The password of the user")

"""
    Define the Schema for the table user to use like a json object
    This class use the BaseModel to inherit the fields of the table
    And also represents an output of the model
    Attributes:
        id: indicates the id of the user
        created_at: indicates the date of the user
"""
#Literal sólo para gets
class User_outs(User_two):
    id: str = Field(title="The id of the user")
    created_at: datetime = Field(title="The date of creation of the user")

"""
    Define the Schema for the table user to use like a json object
    This class use the BaseModel to inherit the fields of the table
    And also represents an update of the model
"""
#No podemos actualizar dirección y teléfono por motivos de seguridad
class User_update(User):
    pass



