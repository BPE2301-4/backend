from ..core import Schedule, session, ResumeTable
from sqlalchemy import select, and_


def filter(post: str | None=None, schedule: Schedule | None=None, education: str | None=None):
    if post == None and schedule == None and education != None:
        return session.query(ResumeTable).where(ResumeTable.education == education)
    elif post == None and schedule != None and education == None:
        return session.query(ResumeTable).where(ResumeTable.schedule == schedule)
    elif post != None and schedule == None and education == None:
        return session.query(ResumeTable).where(ResumeTable.post == post)
    elif post != None and schedule != None and education == None:
        return session.query(ResumeTable).where(and_(ResumeTable.post == post, ResumeTable.schedule == schedule))
    elif post != None and schedule == None and education != None:
        return session.query(ResumeTable).where(and_(ResumeTable.post == post, ResumeTable.education == education))
    elif post == None and schedule != None and education != None:
        return session.query(ResumeTable).where(and_(ResumeTable.schedule == schedule, ResumeTable == education))
    elif post == None and schedule == None and education == None:
        return session.query(ResumeTable)
    else:
        return session.query(ResumeTable).where(and_(ResumeTable.post== post, ResumeTable.schedule == schedule, ResumeTable.education == education))
    #filtered = session.execute(filtered_table)
    #return filtered_table
