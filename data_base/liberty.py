from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .basa_meta import Base

class Liberty(Base):
    __tablename__ = "liberty"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"))

    # liberties = relationship("Liberty_word", back_populates="liberty")
    # user = relationship("User", back_populates="liberty")
