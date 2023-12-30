from sqlalchemy import Column, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship

from  database import Base

class Trip(Base):
    __tablename__ = "trip"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    driver_id = Column(Integer, ForeignKey("driver.id"))
    departure_time  = Column(DateTime, index=True, nullable=False)

    driver = relationship("Driver", back_populates="trips")