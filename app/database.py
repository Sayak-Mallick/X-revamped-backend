from sqlalchemy import create_engine, make_url
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:872320022@localhost:5432/fastapi"

engine = create_engine(
    make_url(SQLALCHEMY_DATABASE_URL).set(drivername="postgresql+psycopg2")
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
