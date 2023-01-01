from sqlalchemy.orm import Session
from database import models , schemas
from database.models import *
from auth import hashing
from datetime import date
from sqlalchemy import and_


# SqlAlchemy ORM query to get all users.
def get_user(db: Session, user_name: str):
    return db.query(User).filter(models.User.Name == user_name).first()

def get_users(db: Session):
    users = db.query(models.User).all()
    return users

# SqlAlchemy ORM query to create a new user.
def create_user(db: Session, user: schemas.UserSchema):
    db_user = User(Name=user.Name,Password = hashing.get_password_hash(user.Password),Role=user.Role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    me = get_user(db, user.Name)
    return me

# SqlAlchemy ORM query to delete any user.
def del_user(db: Session,user_id:str):
    db.query(models.User).filter(models.User.id == user_id).delete()
    db.commit()
    return {"msg":"User deleted successfully"}

# SqlAlchemy ORM query to create a new Book
def create_book(db: Session, book: schemas.BookSchema):
    db_lib = Book(Title=book.Title, Author = book.Author, Publication = book.Publication,Subject=book.Subject,No_of_copies=book.No_of_copies)
    db.add(db_lib)
    db.commit()
    db.refresh(db_lib)
    
def get_books(db: Session):
    books = db.query(models.Book).all()
    return books  

def get_book(db: Session, book_name: str, author:str):
    book = db.query(models.Book).filter(models.Book.Title == book_name, models.Book.Author==author).first()
    if book is not None:
        return book
    else:
        return {"message":"Book Not Found" }
        


def issue_book(db: Session, book: schemas.BookSchema):
    db.query(models.Book).filter(models.Book.Title == book.Title).update({models.Book.No_of_copies : models.Book.No_of_copies-1}, synchronize_session = False) 
    db.commit()
    return {"msg":"book has been issued for you"}

def del_book(db: Session, id:str):
    db.query(models.Issue_table).filter(models.Issue_table.Book_id == id).delete()
    db.query(models.Book).filter(models.Book.id == id).delete()
    db.commit()

def issue_details(db: Session, book:schemas.BookSchema, user_id:str, book_id:str, return_date:date ):
    db_details = Issue_table(Book_id = book_id , Stu_id=user_id, Issue_date=date.today(), Return_date=return_date)
    db.add(db_details)
    db.commit()
    db.refresh(db_details)
    

    




