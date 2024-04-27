from ..core import Resume


def left_column(resume: Resume):
    text_to_write = f"""
    Имя: {resume.name}
    Телефон: {resume.phone}
    Email: {resume.email}
    Дата рождения: {resume.birth_date}
    """
    if resume.city:
        text_to_write += f"Город: {resume.city}\n"
    if resume.citizenship:
        text_to_write += f"Гражданство: {resume.citizenship}\n"
    return text_to_write


def right_column(resume: Resume):
    text_to_write = f"""
        Опыт работы: {resume.work_experience}
        Должность: {resume.post}
        Заработная плата: {resume.salary}
        Занятость: {resume.employment}
        График: {resume.schedule}
        Образование: {resume.education}
        """
    if resume.about:
        text_to_write += f"О себе: {resume.about}\n"
    return text_to_write
