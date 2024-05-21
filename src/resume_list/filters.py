from ..core import Schedule, session, ResumeTable
from sqlalchemy import select, and_


def filter(post: str | None=None, schedule: Schedule | None=None, education: str | None=None):
    if post == None and schedule == None and education != None:
        filtered_table = session.query(ResumeTable).filter(ResumeTable.education == education)
    elif post == None and schedule != None and education == None:
        filtered_table = session.query(ResumeTable).filter(ResumeTable.schedule == schedule)
    elif post != None and schedule == None and education == None:
        filtered_table = session.query(ResumeTable).filter(ResumeTable.post == post)
    elif post != None and schedule != None and education == None:
        filtered_table = session.query(ResumeTable).filter(and_(ResumeTable.post == post, ResumeTable.schedule == schedule))
    elif post != None and schedule == None and education != None:
        filtered_table = session.query(ResumeTable).filter(and_(ResumeTable.post == post, ResumeTable.education == education))
    elif post == None and schedule != None and education != None:
        filtered_table = session.query(ResumeTable).filter(and_(ResumeTable.schedule == schedule, ResumeTable == education))
    elif post == None and schedule == None and education == None:
        filtered_table = session.query(ResumeTable).all()
    else:
        filtered_table = session.query(ResumeTable).filter(and_(ResumeTable.post== post, ResumeTable.schedule == schedule, ResumeTable.education == education))
    filtered = session.execute(filtered_table)
    return filtered
