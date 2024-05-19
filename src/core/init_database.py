# import from folder 'src/core/'
from .database import engine
# import from folder 'src/core/models/'
from .models.base import Base

def init_db():
    try:
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        print("Database initialized successfully!")
    except Exception as e:
        print(f"Error initializing database: {e}")
