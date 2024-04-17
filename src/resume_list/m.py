from ..core import Resume, ResumeTable


def all_or_one_resumes(table: Resume, id: int | None = None):
    if id == 'None':
        return session.query(table).all()
    else:
        select(Resume).where(Resume.id == id)
        result = session.execute(query)
        return result.all()
    
def create_resume(new_resume: Resume):
    session.add(new_resume)
    session.commit()
    return new_resume