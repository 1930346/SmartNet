from pydantic import BaseModel

class Rol(BaseModel):
    id: str | None = None
    name: str
    description: str
    