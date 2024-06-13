from sqlalchemy import Column, Integer, String, ForeignKey
from app.utils.database import Base

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    discussion_id = Column(Integer, ForeignKey('discussions.id'))
