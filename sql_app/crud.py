from sqlalchemy.orm import Session

from . import models, schemas



# users operations
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).one_or_none()

def get_users(db: Session):
    return db.query(models.User).all()

def create_user(db: Session, user: schemas.CreateUser):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user: schemas.User):
    db_user = get_user(db, user.id)
    if db_user is None:
        return None
    
    for var, value in vars(user).items():
        setattr(db_user, var, value) if value else None

    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if db_user is None:
        return
    
    db.delete(db_user)
    db.commit()

# drivers operations
def get_driver(db: Session, driver_id: int):
    return db.query(models.Driver).filter(models.Driver.id == driver_id).first()

def get_drivers(db: Session):
    return db.query(models.Driver).all()

def create_driver(db: Session, driver: schemas.Driver):
    db_driver = models.Driver(**driver.dict())
    db.add(db_driver)
    db.commit()
    db.refresh(db_driver)
    return db_driver

def update_driver(db: Session, driver: schemas.Driver):
    db_driver = get_driver(db, driver.id)
    if db_driver is None:
        return None
    
    for var, value in vars(driver).items():
        setattr(db_driver, var, value) if value else None

    db.commit()
    db.refresh(db_driver)
    return db_driver

def delete_driver(db: Session, driver_id: int):
    db_driver = get_driver(db, driver_id)
    if db_driver is None:
        return
    
    db.delete(db_driver)
    db.commit()

# trips operations
def get_trip(db: Session, trip_id: int):
    return db.query(models.Trip).filter(models.Trip.id == trip_id).first()

def get_trips(db: Session):
    return db.query(models.Trip).all()

def create_trip(db: Session, trip: schemas.CreateTrip):
    db_trip = models.Trip(**trip.dict())
    db.add(db_trip)
    db.commit()
    db.refresh(db_trip)
    return db_trip

def update_trip(db: Session, trip: schemas.Trip):
    db_trip = get_trip(db, trip.id)
    if db_trip is None:
        return None
    
    for var, value in vars(trip).items():
        setattr(db_trip, var, value) if value else None

    db.commit()
    db.refresh(db_trip)
    return db_trip

def delete_trip(db: Session, trip_id: int):
    db_trip = get_trip(db, trip_id)
    if db_trip is None:
        return
    
    db.delete(db_trip)
    db.commit()