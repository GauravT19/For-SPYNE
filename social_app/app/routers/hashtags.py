from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utils.database import get_db
from app.models.hashtag import Hashtag
from app.schemas.hashtag import HashtagCreate, HashtagRead

router = APIRouter(
    prefix="/hashtags",
    tags=["hashtags"]
)

@router.post("/", response_model=HashtagRead)
def create_hashtag(hashtag: HashtagCreate, db: Session = Depends(get_db)):
    db_hashtag = Hashtag(**hashtag.dict())
    db.add(db_hashtag)
    db.commit()
    db.refresh(db_hashtag)
    return db_hashtag

@router.get("/", response_model=list[HashtagRead])
def read_hashtags(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    hashtags = db.query(Hashtag).offset(skip).limit(limit).all()
    return hashtags
