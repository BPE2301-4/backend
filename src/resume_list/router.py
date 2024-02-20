from fastapi import APIRouter
from . import filters
from .schemas import Resume


router = APIRouter(
    prefix='/examples',
    tags=['Summary list']
)


@router.get('/one')
def get_one_summary(summary_id: int):
    return filters.get_one_resume(summary_id=summary_id)


@router.get('/page{page}')
def get_page_resumes(page: int, number_of_resumes: int):
    list_of_id = []
    for i in range(number_of_resumes, number_of_resumes*page):
        list_of_id.append(i)
    return filters.get_several_resumes(list_of_summary_id=list_of_id)


@router.get('/all')
def get_all_resumes():
    return filters.get_all_resumes()


@router.post('/create')
def create_resume(resume: Resume):
    return filters.create_resume(new_resume=resume)
