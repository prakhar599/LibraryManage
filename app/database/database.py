from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# SQLALCHEMY_DATABASE_URL = "sqlite:///D:/folksMediaTasks/LibManageSys/app/database/sql_app.db"
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/LibraryManagementSystem"

engine = create_engine(
    DATABASE_URL, echo = True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
