from sqlalchemy.orm import Session
from database import models , schemas
from database.models import *
from auth import hashing
from datetime import date
from sqlalchemy import and_


# SqlAlchemy ORM query to get details of a single user.
def get_user(db: Session, user_name: str):
    return db.query(User).filter(models.User.Name == user_name).first()

# SqlAlchemy ORM query to get all users.
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
    db.query(models.Issue_table).filter(models.Issue_table.Stu_id == user_id).delete()
    db.query(models.User).filter(models.User.id == user_id).delete()
    db.commit()
    return {"msg":"User deleted successfully"}

# SqlAlchemy ORM query to create a new Book
def create_book(db: Session, book: schemas.BookSchema):
    db_lib = Book(Title=book.Title, Author = book.Author, Publication = book.Publication,Subject=book.Subject,No_of_copies=book.No_of_copies)
    db.add(db_lib)
    db.commit()
    db.refresh(db_lib)
 
# SqlAlchemy ORM query to get all books.   
def get_books(db: Session):
    books = db.query(models.Book).all()
    return books  

# SqlAlchemy ORM query to get details of a single book.
def get_book(db: Session, book_name: str, author:str):
    book = db.query(models.Book).filter(models.Book.Title == book_name, models.Book.Author==author).first()
    if book is not None:
        return book
    else:
        return {"message":"Book Not Found" }

# SqlAlchemy ORM query to issue book for a user.
def issue_book(db: Session, book_id: str):
    db.query(models.Book).filter(models.Book.id == book_id).update({models.Book.No_of_copies : models.Book.No_of_copies-1}, synchronize_session = False) 
    db.commit()
    return {"msg":"book has been issued for you"}


# SqlAlchemy ORM query for return opearation performed by any user.
def return_book(db: Session, book_id: str, user_id: str):
    db.query(models.Issue_table).filter(models.Issue_table.Book_id == book_id, models.Issue_table.Stu_id == user_id).update({models.Issue_table.Return_date : date.today()}, synchronize_session = False)
    db.query(models.Book).filter(models.Book.id == book_id).update({models.Book.No_of_copies : models.Book.No_of_copies+1}, synchronize_session = False) 
    db.commit()
    return {"msg":"Your book has been returned. Thanks for using our Library:D"}


# SqlAlchemy ORM query to delete book from database.
def del_book(db: Session, id:str):
    db.query(models.Issue_table).filter(models.Issue_table.Book_id == id).delete()
    db.query(models.Book).filter(models.Book.id == id).delete()
    db.commit()
  
  
# SqlAlchemy ORM query to update details of any book.    
def update_book(db: Session, book: schemas.BookSchema):
    db.query(models.Book).filter(models.Book.Title == book.Title).update({models.Book.Title : book.Title, models.Book.Author : book.Author, models.Book.Subject : book.Subject, models.Book.Author : book.Author, models.Book.No_of_copies : book.No_of_copies}, synchronize_session = False) 
    db.commit()    
    

# SqlAlchemy ORM query to insert issue details for a single issue operation performed.
def issue_details(db: Session, user_id:str, book_id:str ):
    db_details = Issue_table(Book_id = book_id , Stu_id=user_id, Issue_date=date.today(), Return_date = None)
    db.add(db_details)
    db.commit()
    db.refresh(db_details)
 
 
# SqlAlchemy ORM query to see all transactions perfomed by users in database.   
def show_issue_table(db: Session, skip:int , limit: int):
    return db.query(models.Issue_table).offset(skip).limit(limit).all()
     
    

    




