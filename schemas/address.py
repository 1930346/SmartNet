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

"""
    Define the Schema for the table addresses to use like a json object
    This class inherits from BaseModel and it defines the fields of the table
    Attributes:
        street: indicates the street of the address
        int_number: indicates the number of the address
        ext_number: indicates the number of the address
        colony: indicates the colony of the address
        city: indicates the city of the address
        state: indicates the state of the address
        zip_code: indicates the zip code of the address

"""
class Address(BaseModel):
    street: str = Field(title="The street of the address", max_length=255)
    int_number: str = Field(title="The int_num of the address", max_length= 6)
    ext_number: str = Field(title="The ext_num of the address", max_length= 6)
    colony: str  = Field(title="The colony of the address", max_length=255)
    city: str = Field(title="The city of the address", max_length=255)
    state: str = Field(title="The state of the address", max_length=255)
    zip_code: str = Field(title="The zip_code of the address", max_length = 10)

"""
    Define the Schema for the table addresses to use like a json object
    This class use the BaseModel to inherit the fields of the table
    Attributes:
        user_id: indicates the id of the user that owns the address
"""
class Address_two(Address):
    user_id: str = Field(title="The id of the user")

"""
    Define the Schema for the table addresses to use like a json object
    This class use the BaseModel to inherit the fields of the table
    And also represents an instance of the model
"""
class Address_in(Address_two):
    pass

"""
    Define the Schema for the table addresses to use like a json object
    This class use the BaseModel to inherit the fields of the table
    And also represents an output of the model
    Attributes:
        id: indicates the id of the address
        created_at: indicates the date when the address was created
        modified_at: indicates the date when the address was modified
"""
class Address_outs(Address_two):
    id: str = Field(title="The id of the address") 
    created_at: datetime = Field(title="The date of creation of the address")
    modified_at: datetime = Field(title="The date of modification of the address")

"""
    Define the Schema for the table addresses to use like a json object
    This class use the BaseModel to inherit the fields of the table
    And also represents an update of the model
"""
class Address_update(Address):
    # modified_at: datetime = Field(title="The date of modification of the address")
    pass