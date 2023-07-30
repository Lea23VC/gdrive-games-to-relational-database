from sqlalchemy import Column, Integer, String, Boolean
from config import Base
from sqlalchemy.orm import relationship

class Console(Base):
    __tablename__ = 'consoles'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    fullname = Column(String, nullable=False)
    nasos = Column(Boolean, default=False)

    # Relationship with Game model (one-to-many relationship)
    games = relationship('Game', back_populates='console')
