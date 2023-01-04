from database.schemas import BookSchema, BookIssueSchema, UserSchema
from fastapi import APIRouter, Depends, HTTPException, Body, Query
from database.dbsession import get_db
from auth.auth_handler import signJWT, decodeJWT
from sqlalchemy.orm import Session
import crud
from auth.auth_bearer import JWTBearer
from datetime import date
 


router = APIRouter(
    prefix="/book",
    tags=["Books"],
    responses={
        404: {"description": "Not found"},
        400: {"description": "Invalid request message framing"}
},
)



# get list of all books in db
@router.get("/all")
def get_books(db:Session = Depends(get_db)):
    return crud.get_books(db)

# get details of a single book from db.
@router.get("/get_book")
def get_book(book_name:str, author:str, db:Session = Depends(get_db)): 
    return crud.get_book(db, book_name, author) 

# API endpoint to insert a new book in database schema by librarian
@router.post("/add",dependencies=[Depends(JWTBearer())])
def create_book(db: Session = Depends(get_db),book: BookSchema = Body(...)):
    """
    This endpoint lets you create a new book in database. As you provide `Title` , `Author` , `Publication`,'Subject' and
    `No_of_copies` fields as `BODY()` param. This POST request will insert a new user row in databse schema. 
    Note that only Librarians are authorized and entitled to perform this task.
     
    """
    crud.create_book(db,book=book)
    return {"Response":"successfully added"}


# helper function to get current user in dependency used
def get_current_user(db: Session = Depends(get_db),token: str = Depends(JWTBearer())):
    payload = decodeJWT(token)   
    Name = payload['user_name'] 
    user = crud.get_user(db, user_name = Name)
    return user


@router.post("/issue") #,dependencies=[Depends(JWTBearer())]
def issue_book(*,db: Session = Depends(get_db),current_user: UserSchema = Depends(get_current_user),book_id: str): 
    """
    To get any book issued from library , use this API end point. Any user , be it a librarian or student, can issue book from db.
     
    """
    crud.issue_details(db, user_id = current_user.id, book_id = book_id)
    return crud.issue_book(db, book_id = book_id)

@router.post("/return", dependencies=[Depends(JWTBearer())])
def return_book(*,db: Session = Depends(get_db),current_user: UserSchema = Depends(get_current_user), book_id: str): 
    """
    To return any book of library , use this API end point.
     
    """
    return crud.return_book(db, book_id = book_id, user_id = current_user.id )


@router.delete("/del",dependencies=[Depends(JWTBearer())])
def delete_book(id:str, db: Session = Depends(get_db)):
    """
    This endpoint lets you delete any book from database. As librarian provides `book_id` as QUERY parameter the API
    shall delete it. Note that it's am irreversible process hence can't be undone.     
    """
    crud.del_book(db, id = id)
    return {"Response":"successfully deleted"}

@router.get("/issue_table", dependencies = [Depends(JWTBearer())])
def show_issue_table(
    skip: int | None = Query(default=0, title="Query integer",description="Id of first record"),
    limit: int | None = Query(default=10, title="Query integer",description="Id of last record"),
    db:Session = Depends(get_db)):
    """
    Any user entitled as librarian can use this endpoint to see records of users who has issued books from library.
    just provide `skip` and `limit` values as query parameters to filter out number of
    records that you want to see. and API GET request will handle the rest for you. but make
    sure you authenticate yourself as librarian first in API otherwise you won't be authorized to use it.
    
    """
    return crud.show_issue_table(db, skip, limit)


@router.patch("/edit",dependencies=[Depends(JWTBearer())]) 
def update_book(db: Session = Depends(get_db), book: BookSchema = Body(...)):
    """
    This endpoint will let you update data of books available in db.
     
    """
    crud.update_book(db, book = book) 
    return {"Response":"successfully updated"}
