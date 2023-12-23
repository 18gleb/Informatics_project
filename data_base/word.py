from sqlalchemy import Column, Integer, String, PickleType
from sqlalchemy.orm import relationship

from .basa_meta import Base


class Word(Base):
    __tablename__ = "word"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    on_rus = Column(String, nullable=False)
    on_eng = Column(String, nullable=False)
    how_to_listen = Column(PickleType, nullable=False)
    type_id = Column(Integer, nullable=False)

    libertys = relationship("Liberty_word", back_populates="word")
