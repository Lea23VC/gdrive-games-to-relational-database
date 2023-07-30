from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, Mapped
from config.sqlachemy import Base

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    boxart = Column(String, nullable=False)
    release_date = Column(Date)

    # Foreign key relationship with Console model (many-to-one relationship)
    console_id = Column(Integer, ForeignKey('consoles.id'), nullable=False)
    console: Mapped["Console"] = relationship(back_populates="games")
