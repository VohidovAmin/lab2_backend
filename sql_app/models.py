from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref

from .database import Base

class Driver(Base):
    __tablename__ = "driver"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    last_name = Column(String(30), index=True, nullable=False)
    first_name = Column(String(30), index=True, nullable=False)
    patronymic = Column(String(30), index=True, nullable=False)
    passport = Column(String(10), index=True, nullable=False)
    experience = Column(Date, index=True, nullable=False)

    trips = relationship("Trip", cascade="all, delete-orphan")

class Trip(Base):
    __tablename__ = "trip"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    driver_id = Column(Integer, ForeignKey("driver.id"))
    departure_time  = Column(DateTime, index=True, nullable=False)

    driver = relationship("Driver", back_populates="trips")

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    last_name = Column(String(30), index=True, nullable=False)
    first_name = Column(String(30), index=True, nullable=False)
    patronymic = Column(String(30), index=True, nullable=False)
    group = Column(String(10), index=True, nullable=False)