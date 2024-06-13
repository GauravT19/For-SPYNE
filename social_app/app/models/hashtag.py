from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.utils.database import Base

class Hashtag(Base):
    __tablename__ = 'hashtags'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    discussions = relationship('Discussion', secondary='discussion_hashtag', back_populates='hashtags')
