from sqlalchemy import create_engine
from sqlalchemy_utils.functions import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from server.settings.variables import DB_HOST, DB_PORT, DB_NAME, DB_TYPE, DB_USER, DB_PASS


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


flag = False
if not database_exists(f"{DB_TYPE}://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"):
    flag = True
    create_database(f"{DB_TYPE}://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")


engine = create_engine(f"{DB_TYPE}://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()