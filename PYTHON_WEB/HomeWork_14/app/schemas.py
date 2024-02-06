from pydantic import BaseModel
from datetime import date

class ContactBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    birth_date: date
    additional_data: str = None

class ContactCreate(ContactBase):
    pass

class Contact(ContactBase):
    id: int
    user_id: int  

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str
    contact_limit: int  

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    contacts: list[Contact]  

    class Config:
        from_attributes = True