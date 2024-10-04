import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# MySQL database connection details
DATABASE_URL = "postgresql+psycopg2://default:jBc1tIZFqeX6@ep-tight-leaf-a4k2c60d-pooler.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require"
# DATABASE_URL = os.getenv("DATABASE_URL")

# Create a database engine
engine = create_engine(DATABASE_URL)

# Create a session for interactions with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our models
Base = declarative_base()


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
