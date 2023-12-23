from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from .basa_meta import Base


class Liberty_word(Base):
    __tablename__ = "liberty_word"

    liberty_id = Column(ForeignKey("liberty.id"), primary_key=True)
    word_id = Column(ForeignKey("word.id"), primary_key=True)
    true_or_false = Column(Boolean, nullable=False)

    liberty = relationship("Liberty", back_populates="words")
    word = relationship("Word", back_populates="libertys")
