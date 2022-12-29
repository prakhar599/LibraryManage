from .database import SessionLocal
# Dependency for database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 