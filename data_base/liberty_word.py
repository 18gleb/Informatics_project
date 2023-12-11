from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from .basa_meta import Base

class Liberty_word(Base):
    __tablename__ = "liberty_word"

    liberty_id = Column(Integer, ForeignKey("liberty.id"), nullable=False, primary_key=True)
    word_id = Column(Integer, ForeignKey("word.id"), nullable=False)
    true_or_false = Column(Boolean, nullable=False)

    # liberty = relationship("Liberty", back_populates="liberties")
    # word = relationship("Word", back_populates="liberty")
