# import external libraries
from fastapi import APIRouter, Depends
# import from actual folder
from . import view
from .models import Resume as table_resumes
from .schemas import Resume as scheme_resume

router = APIRouter(
    prefix='/resumes',
    tags=['Filters']
)


@router.get('/id={resume_id}')
def get_one_resume(resume_id: int):
    return view.get_one_resume(resume_id=resume_id)


# @router.get('/page{page}')
# def get_page_resumes(page: int, number_of_resumes: int):
#     list_of_id = []
#     for i in range(number_of_resumes, number_of_resumes*page):
#         list_of_id.append(i)
#     return filters.get_several_resumes(list_of_summary_id=list_of_id)


@router.get('/all')
def get_all_resumes():
    return view.get_all_resumes()


@router.post('/create')
def create_resume(new_resume: scheme_resume):
    return view.create_resume(new_resume=new_resume)
