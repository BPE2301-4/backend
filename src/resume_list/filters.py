from typing import List

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src import get_async_session
from .models import resume
from .schemas import Resume


async def get_one_resume(summary_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(resume).where(resume.c.id == summary_id)
    result = await session.execute(query)
    return result.all()


async def get_several_resumes(list_of_summary_id: List[int], session: AsyncSession = Depends(get_async_session)):
    query = select(resume).filter(resume.id.in_(list_of_summary_id))
    result = await session.execute(query)
    return result.all()


async def get_all_resumes(session: AsyncSession = Depends(get_async_session)):
    query = select(resume)
    result = await session.execute(query)
    return result.all()


async def create_resume(new_resume: Resume, session: AsyncSession = Depends(get_async_session)):
    session.add(new_resume)
    await session.commit()
    return new_resume
