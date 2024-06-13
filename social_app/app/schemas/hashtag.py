from pydantic import BaseModel

class HashtagBase(BaseModel):
    name: str

class HashtagCreate(HashtagBase):
    pass

class HashtagRead(HashtagBase):
    id: int

    class Config:
        orm_mode = True
