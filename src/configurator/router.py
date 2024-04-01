from .schemas import Resume
from fastapi import APIRouter
from src.configurator import create_prompt

router = APIRouter(
    prefix='/configurator',
    tags=['ChatGPT Powered']
)


@router.get('/')
def get_prompt(prompt: str):
    return create_prompt.get_prompt(prompt=prompt)


@router.post('/create')
def get_resume(resume_param: Resume):
    return create_prompt.get_resume(resume_param=resume_param)
