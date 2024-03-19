# import external libraries
from typing import List
from fastapi import Depends
# import sqlalchemy libraries
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
# import from folder 'src' via __init__
from .. import get_async_session
# import from actual folder
from .models import Resume as table_resume
from .schemas import Resume as scheme_resume


async def get_one_resume(resume_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(table_resume).where(table_resume.id == resume_id)
    result = await session.execute(query)
    return result.all()


async def get_several_resumes(list_of_resume_id: List[int], session: AsyncSession = Depends(get_async_session)):
    query = select(table_resume).filter(table_resume.id.in_(list_of_resume_id))
    result = await session.execute(query)
    return result.all()


async def get_all_resumes(session: AsyncSession = Depends(get_async_session)):
    query = select(table_resume)
    result = await session.execute(query)
    return result.all()


async def create_resume(new_resume: scheme_resume, session: AsyncSession = Depends(get_async_session)):
    session.add(new_resume)
    await session.commit()
    return new_resume
