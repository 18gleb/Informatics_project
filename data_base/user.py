from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .basa_meta import Base


class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    mail = Column(String)
    phone = Column(String)
    password = Column(String, nullable=False)
    nickname = Column(String, nullable=False, unique=True)

    liberty = relationship("Liberty", back_populates="user")
