from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_URL = "mysql+pymysql://root:Ngmai2804@localhost:3306/bai1_session18_db"
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(
    autoflush=False,
    expire_on_commit=False,
    bind=engine,
    autocommit=False
)

Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()