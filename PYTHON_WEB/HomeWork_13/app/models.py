from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.database import Base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    contact_limit = Column(Integer, default=10)
    contacts = relationship("Contact", back_populates="user")

class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, index=True)
    phone_number = Column(String, index=True)
    birth_date = Column(Date)
    additional_data = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="contacts")