# db.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Load DB URL from Railway or .env
DATABASE_URL = os.getenv("DATABASE_URL").replace("mysql://", "mysql+pymysql://")
#comment

# Use pymysql for MySQL
engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
