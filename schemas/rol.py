from pydantic import BaseModel, Field

"""
    Define the Schema for the table rol to use like a json object
    This class inherits from BaseModel and it defines the fields of the table
    Attributes:
        name: indicates the name of the order
        description: indicates the description of the order
"""
class Rol(BaseModel):
    # id: str | None = "1"
    name: str = Field(title = "The name of the rol")
    description: str | None = Field(None, title="The description of the rol", max_length=255)

"""
    Define the Schema for the table rol to use like a json object
    This class use the BaseModel to inherit the fields of the table
    And also represents an output of the model
    Attributes:
        id: indicates the id of the rol
"""
class Rol_outs(Rol):
    id: str = Field(title="The id of the rol")

"""
    Define the Schema for the table rol to use like a json object
    This class use the BaseModel to inherit the fields of the table
    And also represents an instance of the model
"""
class Rol_in(Rol):
    pass

"""
    Define the Schema for the table rol to use like a json object
    This class use the BaseModel to inherit the fields of the table
    And also represents an update of the model
"""
class Rol_update(Rol):
    pass