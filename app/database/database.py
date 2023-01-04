from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



DATABASE_URL = "postgresql+psycopg2://postgres:postgres@db:5432/LibraryManagementSystem"
# DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/LibraryManagementSystem"

engine = create_engine(
    DATABASE_URL, echo = True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
