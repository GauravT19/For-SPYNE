from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.utils.database import Base

discussion_hashtag = Table(
    'discussion_hashtag', Base.metadata,
    Column('discussion_id', Integer, ForeignKey('discussions.id')),
    Column('hashtag_id', Integer, ForeignKey('hashtags.id'))
)

class Discussion(Base):
    __tablename__ = 'discussions'
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    image = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_on = Column(String)
    hashtags = relationship('Hashtag', secondary=discussion_hashtag, back_populates='discussions')
