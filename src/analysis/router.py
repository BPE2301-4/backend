# import external libraries
from fastapi import APIRouter
# import from folder 'src/configurator/'
from . import text_updater

router = APIRouter(
    prefix='/analysis',
    tags=['ChatGPT Powered']
)


@router.post('/mistakes')
def get_resume(text: str):
    return text_updater.mist_correction(text=text)
