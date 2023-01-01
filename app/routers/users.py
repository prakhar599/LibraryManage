from fastapi import APIRouter, Depends, HTTPException, Body, Query
from sqlalchemy.orm import Session
from database.schemas import UserSchema, UserLoginSchema
import crud
from auth.auth_handler import signJWT
from auth import hashing
from auth.auth_bearer import JWTBearer
from database.dbsession import get_db
from .books import get_current_user


user_router = APIRouter(
    prefix="/user",
    tags=["Users"],
    responses={
        404: {"description": "Not found"},
        500: {"description":"The server has encountered a situation it does not know how to handle."}
    },
)



# This request is used for creating a new user in database
@user_router.post("/signup")
def create_user(db: Session = Depends(get_db),user: UserSchema = Body(...)):
    """
    This endpoint lets you create a new user in database. As you provide `Name` , `Password` and
    `Role` fields as `BODY()` param. This POST request will insert a new user row in databse schema. 
     
    """
    user = crud.create_user(db,user=user)
    dict = { 
            "user_id" : user.id
        }
    addon = signJWT(user.Name, user.Role)
    dict.update(addon)
    return dict



@user_router.post("/login") 
def read_user(user: UserLoginSchema = Body(...),db: Session=Depends(get_db)):
    """
    This endpoint will let you generate new jwt token for already registered users.
    incase if your token gets expired just use this request and get a new one.
     
    """
    users = crud.get_users(db)
    for ppl in users:   #ppl stands for people
        if ppl.Name == user.Name and hashing.verify_password(user.Password, ppl.Password) :
            return signJWT(ppl.Name, ppl.Role)
    return { "error": "Wrong login details!"} 



#Delete any user by using his ID
@user_router.delete("/{user_id}/del")
def del_user(db: Session = Depends(get_db),current_user: UserSchema = Depends(get_current_user)):
    """
    Delete Your account by passing your ID. Make sure to authenticate yourself first though ;)
     
    """
    return crud.del_user(db, current_user.id)


