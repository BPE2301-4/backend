from fastapi import HTTPException
from ..core import Resume, Font, Text


def left_column(resume: Resume):
    try:
        text_left_column = list()

        if resume.city and resume.citizenship:
            contact_info = Text(
                text=(f"•‎ {resume.email}\n"
                      f"•‎ {resume.phone}\n"
                      f"•‎ {resume.city}, {resume.citizenship}\n"),
                text_padding=3*Font.smpl_left.value.size,
                text_font=Font.smpl_left
            )
        else:
            contact_info = Text(
                text=(f"•‎ {resume.email}\n"
                      f"•‎ {resume.phone}\n"),
                text_padding=2*Font.smpl_left.value.size,
                text_font=Font.smpl_left
            )

        text_left_column.append(contact_info)

        if resume.skills:
            skills_header = Text(
                text="Навыки\n\n",
                text_padding=Font.smpl_left.value.size,
                text_font=Font.bold_left
            )
            text_left_column.append(skills_header)
            skills_text = ''
            c = 0
            for skill in resume.skills:
                skills_text += f'{skill.skill}: {skill.lvl}\n'
                c += 1
            skills = Text(
                text=skills_text,
                text_padding=Font.smpl_left.value.size*c,
                text_font=Font.smpl_left
            )

            text_left_column.append(skills)

        if resume.languages:
            lang_header = Text(
                text='Языки\n\n',
                text_padding=Font.smpl_left.value.size,
                text_font=Font.bold_left
            )
            text_left_column.append(lang_header)
            lang_text = ''
            c = 0
            for lang in resume.languages:
                lang_text += f'{lang.lang}: {lang.lvl}\n'
                c += 1
            langs = Text(
                text=lang_text,
                text_padding=Font.smpl_left.value.size*c,
                text_font=Font.smpl_left
            )
            text_left_column.append(langs)

        if resume.driver_lic:
            driver_header = Text(
                text='Водительские права\n\n',
                text_padding=Font.bold_left.value.size,
                text_font=Font.bold_left
            )
            text_left_column.append(driver_header)
            driver_text = ''
            for cat in resume.driver_lic:
                driver_text += f'{cat.value}   '
            driver_cat = Text(
                text=f'{driver_text}',
                text_padding=Font.smpl_left.value.size,
                text_font=Font.smpl_left
            )
            text_left_column.append(driver_cat)

        return text_left_column

    except AttributeError as ae:
        raise HTTPException(status_code=500, detail=f"Ошибка атрибута: {ae}", headers={"X-Error": "Internal Server Error", "X-Error-Location": "left_column"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Произошла ошибка при формировании левой колонки: {e}", headers={"X-Error": "Internal Server Error", "X-Error-Location": "left_column"})


def right_column(resume: Resume):
    try:
        text_to_right = list()
        if resume.name.patronymic:
            name = Text(
                text=f'{resume.name.surname} {resume.name.name} {resume.name.patronymic}\n',
                text_padding=Font.name.value.size,
                text_font=Font.name
            )
            text_to_right.append(name)
        else:
            name = Text(
                text=f'{resume.name.surname} {resume.name.name}\n',
                text_padding=Font.name.value.size,
                text_font=Font.name
            )
            text_to_right.append(name)

        if resume.post:
            post = Text(
                text=f'{resume.post}\n',
                text_padding=Font.smpl_right.value.size,
                text_font=Font.smpl_right
            )
            text_to_right.append(post)

        if resume.add_inf:
            add_inf = Text(
                text=f'{resume.add_inf}',
                text_padding=Font.smpl_right.value.size,
                text_font=Font.smpl_left,
            )
            text_to_right.append(add_inf)

        text = ''

        if resume.salary:
            text += f'{resume.salary}   '

        if resume.employment:
            text += f'Занятость: {resume.employment.value}   '

        if resume.schedule:
            text += f'График работы: {resume.schedule.value}   '

        if resume.salary or resume.employment or resume.schedule:
            texted = Text(
                text=f'{text}',
                text_padding=Font.smpl_left.value.size,
                text_font=Font.smpl_left
            )
            text_to_right.append(texted)

        if resume.work_exp:
            header = Text(
                text='\nОпыт работы\n',
                text_padding=Font.bold_right.value.size*2,
                text_font=Font.bold_right
            )
            text_to_right.append(header)
            for work in resume.work_exp:
                work_header = Text(
                    text=f'{work.post}',
                    text_padding=Font.bold_right.value.size,
                    text_font=Font.bold_right
                )
                text_to_right.append(work_header)
                work_period = Text(
                    text=f'{work.start_date} - {work.finish_date}\n',
                    text_padding=Font.smpl_left.value.size,
                    text_font=Font.smpl_right
                )
                text_to_right.append(work_period)
                work_place = Text(
                    text=f'{work.place}\n',
                    text_padding=Font.smpl_right.value.size,
                    text_font=Font.smpl_right
                )
                text_to_right.append(work_place)
    except AttributeError as ae:
        raise HTTPException(status_code=500, detail=f"Ошибка атрибута: {ae}", headers={"X-Error": "Internal Server Error", "X-Error-Location": "right_column"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Произошла ошибка при формировании правой колонки: {e}", headers={"X-Error": "Internal Server Error", "X-Error-Location": "right_column"})
