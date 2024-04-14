# import external libraries
from fastapi import APIRouter
from typing import List
# import from folder 'src/core/' via __init__
from ..core import Url
# import from folder 'src/configurator/'
from . import url_writer

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