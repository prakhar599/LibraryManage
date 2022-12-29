from pydantic import BaseModel, Field, EmailStr
from datetime import date

class UserSchema(BaseModel):
    id : str = Field(default=None)
    Name : str = Field(...)
    Password: str = Field(...)
    Role: str = Field(...)  


    class Config:
        schema_extra = {
            "example": {
                "Name": "Joelay field",
                "Password": "any",
                "Role": "user or Librarian"
            }
        }
        orm_mode = True
        
class UserLoginSchema(BaseModel):
    Name: str = Field(...)
    Password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "Name": "sitaram@gmail.com",
                "Password": "any"
            }
        }    
        orm_mode = True

        
class BookSchema(BaseModel):
    id : str = Field(default=None)
    Title: str = Field(...)
    Author: str = Field(...)
    Publication: str = Field(...)
    Subject: str = Field(...)
    No_of_copies: int = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "Title": "sitaram",
                "Author": "any",
                "Publication": "Gita Press",
                "Subject": "Religious",
                "No_of_copies": "2"
            }
        }    
        orm_mode = True 
        
class BookIssueSchema(BaseModel):
    id : str = Field(default=None)
    Title: str = Field(...)
    Author: str = Field(...)
    Publication: str = Field(...)
    No_of_copies: int = Field(...)

 
    class Config:
        schema_extra = {
            "example": {
                "Title": "sitaram",
                "Author": "any",
                "Publication": "Gita Press",
                "No_of_copies": "1"

         }
        }    
        orm_mode = True         
        
class IssueSchema(BaseModel):
    Book_id: str = Field(...)
    Stu_id: str = Field(...)
    Issue_date : date = Field(...)
    Return_date : date = Field()

    class Config:
        schema_extra = {
            "example": {
                "Book_id": "1",
                "Stu_id": "1",
                "Issue_date": "2022-12-21",
            }
        }    
        orm_mode = True      
        
                
             
               