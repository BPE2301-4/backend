# import from folder 'src/core/'
from .database import engine
# import from folder 'src/core/models/'
from .models.base import Base


def init_db():
    with engine.begin() as conn:
        conn(Base.metadata.drop_all)
        conn(Base.metadata.create_all)