from pydantic import BaseModel

class Rol(BaseModel):
    # id: str | None = "1"
    name: str
    description: str | None = None

class Rol_outs(Rol):
    id: str

class Rol_in(Rol):
    pass

class Rol_update(Rol):
    pass