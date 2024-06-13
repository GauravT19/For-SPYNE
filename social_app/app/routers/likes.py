from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utils.database import get_db
from app.models.like import Like
from app.schemas.like import LikeCreate, LikeRead

router = APIRouter(
    prefix="/likes",
    tags=["likes"]
)

@router.post("/", response_model=LikeRead)
def create_like(like: LikeCreate, db: Session = Depends(get_db)):
    db_like = Like(**like.dict())
    db.add(db_like)
    db.commit()
    db.refresh(db_like)
    return db_like

@router.get("/", response_model=list[LikeRead])
def read_likes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    likes = db.query(Like).offset(skip).limit(limit).all()
    return likes
