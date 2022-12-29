from database.schemas import BookSchema , BookIssueSchema
from fastapi import APIRouter, Depends, HTTPException, Body, Query
from database.dbsession import get_db
from auth.auth_handler import signJWT
from sqlalchemy.orm import Session
import crud
from auth.auth_bearer import JWTBearer

router = APIRouter(
    prefix="/book",
    tags=["books"],
    responses={404: {"description": "Not found"}},
)




@router.get("/all")
def get_books(db:Session = Depends(get_db)):
    return crud.get_books(db)

@router.post("/add",dependencies=[Depends(JWTBearer())])
def create_book(db: Session = Depends(get_db),book: BookSchema = Body(...)):
    """
    This endpoint lets you create a new book in database. As you provide `Title` , `Author` , `Publication`,'Subject' and
    `No_of_column` fields as `BODY()` param. This POST request will insert a new user row in databse schema. 
     
    """
    crud.create_book(db,book=book)
    return {"Response":"successfully added"}

@router.post("/issue")
def issue_book(*,db: Session = Depends(get_db),book: BookIssueSchema = Body(...),user_id: str, book_id: str): 
    crud.issue_details(db,book=book, user_id = user_id, book_id = book_id)
    return crud.issue_book(db,book=book)