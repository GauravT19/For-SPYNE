from sqlalchemy.orm import Session
from app.models.user import User  # Adjust as per your module structure
from app.core.security import verify_password  # Adjust as per your module structure

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.password):
        return None
    return user