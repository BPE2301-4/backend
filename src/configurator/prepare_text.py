from ..core import Resume


def left_column(resume: Resume):
    text_to_write = f"""
    Имя: 
    {resume.name}
    Телефон: 
    {resume.phone}
    Email: 
    {resume.email}
    Дата рождения: 
    {resume.birth_date}
    
    """
    if resume.city:
        text_to_write += (f"Город:\n"
                          f"{resume.city}\n"
                          f"\n")
    if resume.citizenship:
        text_to_write += (f"Гражданство:\n"
                          f"{resume.citizenship}\n"
                          f"\n")
    return text_to_write


def right_column(resume: Resume):
    text_to_write = f"""
        Опыт работы:\n {resume.work_exp}
        Должность:\n {resume.post}
        Заработная плата:\n {resume.salary}
        Занятость:\n {resume.employment}
        График:\n {resume.schedule}
        Образование:\n {resume.education}
        """
    if resume.about:
        text_to_write += f"О себе: {resume.about}\n"
    return text_to_write
