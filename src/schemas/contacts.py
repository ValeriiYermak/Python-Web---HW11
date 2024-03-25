
from pydantic import BaseModel, Field, EmailStr


class ContactSchema(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    lastname: str = Field(min_length=3, max_length=50)
    email: EmailStr
    phone: str = Field(min_length=7, max_length=50)
    birthdate: str = Field(min_length=7, max_length=50)
    others_info: str = Field(min_length=5, max_length=250)
    completed: bool


class ContactUpdateSchema(ContactSchema):
    completed: bool


class ContactResponse(BaseModel):
    id: int = 1
    name: str = Field(min_length=3, max_length=50)
    lastname: str = Field(min_length=3, max_length=50)
    email: EmailStr
    phone: str = Field(min_length=7, max_length=50)
    birthdate: str = Field(min_length=7, max_length=50)
    others_info: str = Field(min_length=5, max_length=250)
    completed: bool

    class Config:
        from_attributes = True
