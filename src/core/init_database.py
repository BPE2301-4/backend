# import from folder 'src/core/'
from .database import engine
# import from folder 'src/core/models/'
from .models.base import Base


def init_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
