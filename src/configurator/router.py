from fastapi import HTTPException
import asyncio

from . import create_pdf
from ..core import Resume, Employment, Schedule, Avatar, Name
from fastapi import Form, File, UploadFile, APIRouter
from typing import Optional
from pydantic import EmailStr
from datetime import date
from io import BytesIO
import json

router = APIRouter(
    prefix='/configurator',
    tags=['Create your own resume and download it as PDF-file']
)


@router.post('/create')
def submit_resume(
        surname: str = Form(None, example='Антонов', title='Surname'),
        name: str = Form(None, example='Антон', title='Name'),
        patronymic: Optional[str] = Form(None, example='Антонович', title='Patronymic'),
        phone: str = Form(None, example='8-800-555-35-35', min_length=11, max_length=16, title='Phone number'),
        email: EmailStr = Form(None, example='example@example.com', title='Email'),
        work_exp: Optional[str] = Form(None, title='Work experience', description='List of JSON object'),  # We will parse this from JSON
        birth_date: Optional[date] = Form(None, format='YYYY-MM-DD', title='Birth date'),
        city: Optional[str] = Form(None, title='City'),
        citizenship: Optional[str] = Form(None, title='Citizenship'),
        post: Optional[str] = Form(None, title='Post'),
        salary: Optional[str] = Form(None, title='Salary'),
        employment: Optional[Employment] = Form(None, examples=[Employment.full, Employment.partial, Employment.project, Employment.volunteering, Employment.intership], title='Employment', description='Can be only: full, partial, project, volunteering, intership, None'),
        schedule: Optional[Schedule] = Form(None, examples=[Schedule.full, Schedule.shift, Schedule.flexible, Schedule.remote, Schedule.watch], title='Schedule', description='Can be only: full, shift, flexible, remote, watch, None'),
        education: Optional[str] = Form(None, title='Educattion', description='List of JSON objects'),  # We will parse this from JSON
        languages: Optional[str] = Form(None, title='Languages', description='List of JSON objects'),  # We will parse this from JSON
        driver_lic: Optional[str] = Form(None, title='Driver license', description='List of Enum'),  # We will parse this from JSON
        skills: Optional[str] = Form(None, title='Skills', description='List of JSON objects'),  # We will parse this from JSON
        add_inf: Optional[str] = Form(None, title='Additional information'),
        avatar_file: UploadFile = File(None, title='Avatar', description='Only square photo'),
        avatar_url: Optional[str] = Form(None, title='Avatar', description='Link to photo'),
        template_image: int = Form(..., title='Number of template', description='We have only one template with id=1')
):
    try:
        work_exp_list = json.loads(work_exp) if work_exp else None
        education_list = json.loads(education) if education else None
        languages_list = json.loads(languages) if languages else None
        driver_lic_list = json.loads(driver_lic) if driver_lic else None
        skills_list = json.loads(skills) if skills else None

        resume = Resume(
            name=Name(surname=surname, name=name, patronymic=patronymic),
            phone=phone,
            email=email,
            work_exp=work_exp_list,
            birth_date=birth_date,
            city=city,
            citizenship=citizenship,
            post=post,
            salary=salary,
            employment=employment,
            schedule=schedule,
            education=education_list,
            languages=languages_list,
            driver_lic=driver_lic_list,
            skills=skills_list,
            add_inf=add_inf
        )
        if avatar_file:
            if avatar_file.content_type not in ["image/png", "image/jpeg"]:
                raise HTTPException(status_code=400, detail="Формат файла должен быть PNG или JPEG")
            else:
                async def read_avatar_file():
                    return await avatar_file.read()

                content = asyncio.run(read_avatar_file())
                image_bytes = BytesIO(content)
                avatar = Avatar(file=image_bytes.getvalue())
                resume.avatar = avatar
        elif avatar_url:
            avatar = Avatar(url=avatar_url)
            resume.avatar = avatar
        return create_pdf.generate_pdf(resume=resume, template_image=template_image)
    except json.JSONDecodeError as jde:
        raise HTTPException(status_code=422, detail="Ошибка разбора JSON", headers={"X-Error": "Unprocessable Entity", "X-Error-Location": "submit_resume"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Внутренняя ошибка сервера: {e}", headers={"X-Error": "Internal Server Error", "X-Error-Location": "submit_resume"})
