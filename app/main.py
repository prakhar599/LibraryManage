from fastapi import Depends,FastAPI
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database import models
from database.database import SessionLocal, engine
from routers.users import user_router
from routers.books import router


# Security for API
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
models.Base.metadata.create_all(bind=engine)



        

tags_metadata = [
    {
        "name": "Users",
        "description": "Operations for User Managment",
        "externalDocs": {
            "description": "Users external docs",
            "url": "https://fastapi.tiangolo.com/",
        }
    },
    
    {
        "name": "Books",
        "description": "Operations for Books Managment",
        "externalDocs": {
            "description": "Users external docs",
            "url": "https://fastapi.tiangolo.com/",
        }
    },  
]

# description to be used in API metadata       
description = """
Library Management API helps you automate library functions in a secure way. 
This API provides a good exposure to its functionalities Even for a layman 
and it makes it very handy to deal with Users ,Librarians and Books' data in back-end. 🚀

## Library Management API
Operations that can be performed:
* **Create users**
* **Create Librarians**
* **Get Book details from DB** 
* **Inserting New Books in DB** 
* **Update users' credentials( Refreshing of Tokens )** 
* **Delete users** 
* **Issuing book** 

"""   
 
app = FastAPI( title="Library Management App",
    description=description,
    version="0.0.1",
    openapi_tags=tags_metadata
)
app.include_router(router)
app.include_router(user_router)





