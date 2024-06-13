from pydantic import BaseModel

class LikeBase(BaseModel):
    user_id: int
    discussion_id: int

class LikeCreate(LikeBase):
    pass

class LikeRead(LikeBase):
    id: int

    class Config:
        orm_mode = True
