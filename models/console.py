from sqlalchemy import Column, Integer, String, Boolean
from config.sqlachemy import Base
from sqlalchemy.orm import relationship, Mapped
from typing import List
from models.game import Game

class Console(Base):
    __tablename__ = 'consoles'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    fullname = Column(String, nullable=False)
    nasos = Column(Boolean, default=False)

    # Relationship with Game model (one-to-many relationship)
    games: Mapped[List["Game"]] = relationship()
