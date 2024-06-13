from passlib.context import CryptContext

# Secret key to sign JWT tokens
SECRET_KEY = "local"  
ALGORITHM = "HS256"

# Create a CryptContext instance with bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Function to hash a password
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Function to verify a password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
