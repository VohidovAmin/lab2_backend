from typing import Any
from typing import Generator

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
#this is to include backend dir in sys.path so that we can import from db,main.py

from app.database import get_db
from app.config import POSTGRES_TEST_DATABASE_URL

print("HERE0 AAAAAAAAAAAAAAAAAAAAAAAAAAAA -------------------")
print(POSTGRES_TEST_DATABASE_URL)
engine = create_engine(POSTGRES_TEST_DATABASE_URL)
SessionTesting = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def app() -> Generator[FastAPI, Any, None]:
    print("HERE -------------------")
    from app.main import app
    """
    Create a fresh database on each test case.
    """
    Base = declarative_base()
    Base.metadata.create_all(engine)  # Create the tables.
    
    yield app
    Base.metadata.drop_all(engine)

@pytest.fixture(scope="function")
def db_session(app: FastAPI) -> Generator[SessionTesting, Any, None]:
    print("HERE1 -------------------")
    connection = engine.connect()
    transaction = connection.begin()
    session = SessionTesting(bind=connection)
    yield session  # use the session in tests.
    session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture(scope="function")
def client(app: FastAPI, db_session: SessionTesting) -> Generator[TestClient, Any, None]:
    print("HERE2 -------------------")
    """
    Create a new FastAPI TestClient that uses the `db_session` fixture to override
    the `get_db` dependency that is injected into routes.
    """

    def _get_test_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = _get_test_db
    with TestClient(app, base_url="http://127.0.0.1:9000") as client:
        yield client