# import external libraries
from fastapi import FastAPI
# import from folder 'resume_list' via __init__
from .resume_list import router as summary_list_router
# import from actual folder
from .database import init_db
from .resume_list import Resume

app = FastAPI(
    title='JobJotter'
)


@app.get('/init_database')
async def init_database():
    await init_db()


app.include_router(
    summary_list_router,
    prefix='/public'
)
