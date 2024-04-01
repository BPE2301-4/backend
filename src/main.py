# import external libraries
from fastapi import FastAPI
# import from folder 'resume_list' via __init__
from .resume_list import router as resume_list_router
# import from folder 'configurator' via __init__
from .configurator import router as configurator_router
# import from actual folder
from .database import init_db
from .resume_list import Resume

app = FastAPI(
    title='JobJotter'
)


@app.get('/init_database')
def init_database():
    init_db()


app.include_router(
    resume_list_router,
    prefix='/public'
)


app.include_router(
    configurator_router,
    prefix='/public'
)
