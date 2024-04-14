def all_or_one_resumes(table: Resume, id: int | None = None):
    if id == 'None':
        return session.query(table).all()
    else:
        select(Resume).where(Resume.id == id)
        result = session.execute(query)
        return result.all()
    