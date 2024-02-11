import uvicorn
from fastapi import FastAPI

app = FastAPI(title='testname_summary')

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
