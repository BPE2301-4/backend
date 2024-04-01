# import external libraries
from typing import List
# import sqlalchemy libraries
from sqlalchemy import select
# import from folder 'src' via __init__
from .. import session
# import from actual folder
from .models import Resume as table_resume
from .schemas import Resume as scheme_resume


def get_one_resume(resume_id: int):
    query = select(table_resume).where(table_resume.id == resume_id)
    result = session.execute(query)
    return result.all()


def get_several_resumes(list_of_resume_id: List[int]):
    query = select(table_resume).filter(table_resume.id.in_(list_of_resume_id))
    result = session.execute(query)
    return result.all()


def get_all_resumes():
    query = select(table_resume)
    result = session.execute(query)
    return result.all()


def create_resume(new_resume: scheme_resume):
    session.add(new_resume)
    session.commit()
    return new_resume
