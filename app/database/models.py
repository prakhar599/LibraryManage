from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from .database import Base
import uuid


def generate_uuid():
    return str(uuid.uuid4())


class User(Base):
    __tablename__ = "users"
    id = Column(String, name="uuid", primary_key=True, default=generate_uuid)
    Name = Column(String)
    Password = Column(String)  
    Role = Column(String)
    
class Book(Base):
    __tablename__ = "books"
    id = Column(String, name="uuid", primary_key=True, default=generate_uuid)
    Title = Column(String)    
    Author = Column(String) 
    Publication = Column(String) 
    Subject =  Column(String)
    No_of_copies = Column(Integer)
    
    
class Issue_table(Base):
    __tablename__ = "Issue_table"
    id = Column(String, name="uuid", primary_key=True, default=generate_uuid)
    Book_id = Column(String, ForeignKey(Book.id))  
    Stu_id = Column(String, ForeignKey(User.id))      
    Issue_date = Column(Date)
    Return_date = Column(Date)

    
    
    
    
    
    

