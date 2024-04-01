# import sqlalchemy libraries
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
# import from folder 'src'
from .config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
Base = declarative_base()
metadata = Base.metadata


engine = create_engine(DATABASE_URL)
Session = sessionmaker(engine, expire_on_commit=False)
session = Session()


def init_db():
    with engine.begin() as conn:
        conn(Base.metadata.drop_all)
        conn(Base.metadata.create_all)


# def get_session():
#     with Session() as session:
#         return session
        