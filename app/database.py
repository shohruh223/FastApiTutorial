from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# postgresql://username:password@host:port/database_name
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost:5432/testdb"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
