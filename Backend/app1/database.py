from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Backend.app1.adapter.orm import Base

DATABASE_URL = "sqlite:///C:/Users/dell/Desktop/HostelManagementSystem/Backend/testing.db"

engine = create_engine(
    DATABASE_URL,
    echo=True,
    connect_args={"check_same_thread": False}
)
sessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
