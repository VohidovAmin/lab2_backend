from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    last_name = Column(String(30), index=True, nullable=False)
    first_name = Column(String(30), index=True, nullable=False)
    patronymic = Column(String(30), index=True, nullable=False)
    group = Column(String(10), index=True, nullable=False)