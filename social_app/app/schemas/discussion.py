from pydantic import BaseModel
from datetime import datetime

class DiscussionBase(BaseModel):
    text: str
    image: str = None
    hashtags: str = None
    created_on: datetime

class DiscussionCreate(DiscussionBase):
    pass

class DiscussionRead(DiscussionBase):
    id: int

    class Config:
        orm_mode = True
