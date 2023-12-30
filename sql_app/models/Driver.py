from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

from  database import Base

class Driver(Base):
    __tablename__ = "driver"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    last_name = Column(String(30), index=True, nullable=False)
    first_name = Column(String(30), index=True, nullable=False)
    patronymic = Column(String(30), index=True, nullable=False)
    passport = Column(String(10, index=True), nullable=False)
    experience = Column(Date, index=True, nullable=False)