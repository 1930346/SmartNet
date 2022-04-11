from pydantic import BaseModel, Field

class Rol(BaseModel):
    # id: str | None = "1"
    name: str = Field(title = "The name of the rol")
    description: str | None = Field(None, title="The description of the rol", max_length=255)

class Rol_outs(Rol):
    id: str = Field(title="The id of the rol")

class Rol_in(Rol):
    pass

class Rol_update(Rol):
    pass