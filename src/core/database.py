# import sqlalchemy libraries
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
# import from folder 'src/'
from ..config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER
# import from folder 'src/core/models/'
from models.base import Base

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

metadata = Base.metadata


engine = create_engine(DATABASE_URL)
Session = sessionmaker(engine, expire_on_commit=False)
session = Session()
