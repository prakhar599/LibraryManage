from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# to verify any plain password with hashed version of it.
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# to get hashed version of any password.
def get_password_hash(password):
    return pwd_context.hash(password)