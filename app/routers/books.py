from database.schemas import BookSchema , BookIssueSchema
from fastapi import APIRouter, Depends, HTTPException, Body, Query
from database.dbsession import get_db
from auth.auth_handler import signJWT
from sqlalchemy.orm import Session
import crud
from auth.auth_bearer import JWTBearer


router = APIRouter(
    prefix="/book",
    tags=["Books"],
    responses={404: {"description": "Not found"}},
)



# get list of all books in db
@router.get("/all")
def get_books(db:Session = Depends(get_db)):
    return crud.get_books(db)

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

@router.post("/issue")
def issue_book(*,db: Session = Depends(get_db),book: BookIssueSchema = Body(...),user_id: str, book_id: str): 
    """
    To get any book issued from library , use this API end point. Any user , be it a librarian or student, can issue book from db.
     
    """
    crud.issue_details(db,book=book, user_id = user_id, book_id = book_id)
    return crud.issue_book(db,book=book)