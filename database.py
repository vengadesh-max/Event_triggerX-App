from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.base import Base

DATABASE_URL = "sqlite:///./test.db"  # Update with your actual database URL

# SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
# Baseconf = declarative_base()


def create_tables():
    """Initializes the database by creating all tables."""
    Base.metadata.create_all(bind=engine)
    print("Database initialized successfully.")


# def init_db():
#     """Wrapper function to initialize the database."""
#     create_tables()


def init_db():
    """Wrapper function to initialize the database."""
    try:
        # Call create_tables to initialize the database and create tables
        create_tables()
        print("Database initialized successfully.")
    except Exception as e:
        print(f"Error initializing the database: {e}")
        raise Exception("Database initialization failed")  # Reraise if needed
