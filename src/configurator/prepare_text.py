from ..core import Resume


def left_column(resume: Resume):
    text_to_write = f"""
    — {resume.phone}\n
    \n
    — {resume.email}\n
    \n
    """
    if resume.city:
        text_to_write += f"""
            {resume.city}
            """
    if resume.citizenship:
        text_to_write += f""" ,{resume.citizenship}\n"""
    if resume.skills:
        text_to_write += f"""Навыки\n
            \n
            """
        for i in resume.skills:
            text_to_write += f"""
                {i.skill}\n
                \n
                {i.lvl}\n
                \n
                """
    if resume.languages:
        text_to_write += f"""Языки\n
            \n
            """
        for i in resume.languages:
            text_to_write += f"""
                {i.lang} ({i.lvl})\n
                \n
                """
    return text_to_write


def right_column(resume: Resume):
    text_to_write = f"""
        {resume.name.surname} {resume.name.name} {resume.name.patronymic}\n
        {resume.post}, предпочитаемая зп: {resume.salary}\n
        \n
        """
    if resume.add_inf:
        text_to_write += f"О себе: {resume.add_inf}\n"
    return text_to_write
