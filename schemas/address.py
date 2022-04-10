from datetime import datetime
from pydantic import BaseModel

# Modelo base
# class address(BaseModel):
#     # id: str | None = None
#     user_id: str
#     street: str
#     int_num: str
#     ext_num: str
#     colony: str
#     city: str
#     state: str
#     zip_code: str
#     created_at: datetime | None = None
#     modified_at: datetime | None = None


class Address(BaseModel):
    street: str
    int_num: str
    ext_num: str
    colony: str
    city: str
    state: str
    zip_code: str

class Address_two(Address):
    user_id: str

class Address_in(Address_two):
    pass

class Address_outs(Address_two):
    id: str
    created_at: datetime
    modified_at: datetime

class Address_update(Address):
    modified_at: datetime
    pass