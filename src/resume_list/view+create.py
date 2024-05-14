from ..core import ResumeForTable, ResumeTable, session


def all_or_one_resumes(id: int | None = None):
    if id == 'None':
        return session.query(ResumeTable).all()
    else:
        query = session.select(ResumeTable).where(ResumeTable.id == id)
        result = session.execute(query)
        return result.all()
    
def create_resume(new_resume: ResumeForTable):
     resume = ResumeTable(
        name=new_resume.name,
        phone=new_resume.phone,
        email=new_resume.email,
        work_exp=new_resume.work_exp,
        birth_date=new_resume.birth_date,
        city=new_resume.city,
        citizenship=new_resume.citizenship,
        post=new_resume.post,
        salary=new_resume.salary,
        employment=new_resume.employment,
        schedule=new_resume.schedule,
        education=new_resume.education,
        about=new_resume.about
    )
    session.add(resume)
    session.commit()
    return new_resume