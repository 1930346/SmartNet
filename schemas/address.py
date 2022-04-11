from datetime import datetime
from pydantic import BaseModel, Field

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
    street: str = Field(title="The street of the address", max_length=255)
    int_num: str = Field(title="The int_num of the address", max_length= 6)
    ext_num: str = Field(title="The ext_num of the address", max_length= 6)
    colony: str  = Field(title="The colony of the address", max_length=255)
    city: str = Field(title="The city of the address", max_length=255)
    state: str = Field(title="The state of the address", max_length=255)
    zip_code: str = Field(title="The zip_code of the address", max_length = 10)

class Address_two(Address):
    user_id: str = Field(title="The id of the user")

class Address_in(Address_two):
    pass

class Address_outs(Address_two):
    id: str = Field(title="The id of the address") 
    created_at: datetime = Field(title="The date of creation of the address")
    modified_at: datetime = Field(title="The date of modification of the address")

class Address_update(Address):
    modified_at: datetime = Field(title="The date of modification of the address")
    pass