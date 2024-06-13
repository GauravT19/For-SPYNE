from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utils.database import get_db
from app.models.discussion import Discussion
from app.schemas.discussion import DiscussionCreate, DiscussionRead

router = APIRouter(
    prefix="/discussions",
    tags=["discussions"]
)

@router.post("/", response_model=DiscussionRead)
def create_discussion(discussion: DiscussionCreate, db: Session = Depends(get_db)):
    db_discussion = Discussion(**discussion.dict())
    db.add(db_discussion)
    db.commit()
    db.refresh(db_discussion)
    return db_discussion

@router.get("/", response_model=list[DiscussionRead])
def read_discussions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    discussions = db.query(Discussion).offset(skip).limit(limit).all()
    return discussions

@router.get("/search/", response_model=list[DiscussionRead])
def search_discussions(text: str, db: Session = Depends(get_db)):
    discussions = db.query(Discussion).filter(Discussion.text.contains(text)).all()
    return discussions
