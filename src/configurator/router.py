# importt extternal libraries
from fastapi import APIRouter
# import from folder 'src/core/' via __init__
from ..core import Resume
# import from folder 'src/configurator/'
from ..configurator import create_prompt

router = APIRouter(
    prefix='/configurator',
    tags=['ChatGPT Powered']
)


@router.post('/create')
def get_resume(resume_param: Resume):
    return create_prompt.get_resume(resume_param=resume_param)
