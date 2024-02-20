from fastapi import FastAPI
from .resume_list import router as list_router


app = FastAPI(title='testname_summary')


@app.get('/')
def root():
    return 'hello!'


app.include_router(list_router)
