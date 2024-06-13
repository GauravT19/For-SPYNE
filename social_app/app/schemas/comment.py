from pydantic import BaseModel

class CommentBase(BaseModel):
    text: str
    user_id: int
    discussion_id: int

class CommentCreate(CommentBase):
    pass

class CommentRead(CommentBase):
    id: int

    class Config:
        orm_mode = True
