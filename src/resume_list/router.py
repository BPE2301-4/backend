# import external libraries
from fastapi import APIRouter
from typing import List
# import from folder 'src/core/' via __init__
from ..core import Url, Resume
# import from folder 'src/configurator/'
from . import url_writer
from .m import all_or_one_resumes, create_resume

router = APIRouter(
    prefix='/resume_list',
    tags=['View and filter resume examples']
)


@router.post('/append_one_resume_url')
def append_one_url(url: str):
    return url_writer.append_one_url(url=url)


@router.post('/append_many_url')
def append_many_url(list_of_url: List[str]):
    return url_writer.append_many_url(list_of_url=list_of_url)


@router.post('request')
def get_url_from_request(post: str):
    return url_writer.get_url_from_request(post=post)

@router.post('/all_or_one_resume')
def all_or_one_resume(table: Resume, id: int | None=None):
    return all_or_one_resumes(table=table, id=id)


@router.post('/create')
def create_resumes(new_resume: Resume):
    return create_resume(new_resume=new_resume)