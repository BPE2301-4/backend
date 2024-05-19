# import external libraries
from fastapi import FastAPI
# import from folder 'src/resume_list/' via __init__
from .resume_list import router as resume_list_router
# import from folder 'src/configurator/' via __init__
from .configurator import router as configurator_router
# import from folder 'src/core/' via __init__
from .core import init_db
# import from folder 'src/analysis/' via __init__
from .analysis import router as analisys_router

app = FastAPI(
    title='JobJotter'
)


@app.get('/init_database')
def init_database():
    init_db()


app.include_router(
    configurator_router,
    prefix='/public'
)


app.include_router(
    resume_list_router
)

app.include_router(
    analisys_router
)
