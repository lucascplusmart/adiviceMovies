from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

class DatabaseConfig:
    def __init__(self):
        self.DATABASE_URL = "sqlite:///./database.db"
        self.engine = create_engine(
            self.DATABASE_URL, connect_args={"check_same_thread": False}
        )
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.Base = declarative_base()

# Instância global
db_config = DatabaseConfig()