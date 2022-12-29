from sqlalchemy.orm import Session
from database import models , schemas
from database.models import *
from auth import hashing
from datetime import date


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
    author = db.query(models.Book).all()
    return author  


def issue_book(db: Session, book: schemas.BookSchema):
    db.query(models.Book).filter(models.Book.Title == book.Title).update({models.Book.No_of_copies : models.Book.No_of_copies-1}, synchronize_session = False) 
    db.commit()
    return {"msg":"book has been issued for you"}

def issue_details(db: Session, book:schemas.BookSchema, user_id:str, book_id:str ):
    db_details = Issue_table(Book_id = book_id , Stu_id=user_id, Issue_date=date.today())
    db.add(db_details)
    db.commit()
    db.refresh(db_details)
    

    




