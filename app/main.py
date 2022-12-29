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
        "name": "users",
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
Library Management API helps you register users in database in a secure way . 🚀

## Users
Operations that can be performed:
* **Get users from DB** 
* **Get Librarians from DB** 
* **Create users**
* **Create Librarians**
* **Get Book details from DB** 
* **Update users' credentials** 
* **Delete users** 
* **Issuing book** 

"""   
 
app = FastAPI( title="Librarian Management App",
    description=description,
    version="0.0.1",
    openapi_tags=tags_metadata
)
app.include_router(router)
app.include_router(user_router)





