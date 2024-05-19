# import external libraries
import asyncio

from . import create_pdf
from ..core import Resume, Employment, Schedule, Avatar, Name, WorkExp, Education, Languages, Skills, DriverLicense
from fastapi import Form, File, UploadFile, APIRouter
from typing import Optional, List
from pydantic import EmailStr
from datetime import date
from io import BytesIO

Form()

router = APIRouter(
    prefix='/configurator',
    tags=['Create your own resume and download it as PDF-file']
)


@router.post('/create')
def submit_resume(
        surname: str = Form(...),
        name: str = Form(...),
        patronymic: Optional[str] = Form(None),
        phone: str = Form(...),
        email: EmailStr = Form(...),
        work_exp: Optional[str] = Form(None),  # We will parse this from JSON
        birth_date: Optional[date] = Form(None),
        city: Optional[str] = Form(None),
        citizenship: Optional[str] = Form(None),
        post: Optional[str] = Form(None),
        salary: Optional[str] = Form(None),
        employment: Optional[Employment] = Form(None),
        schedule: Optional[Schedule] = Form(None),
        education: Optional[str] = Form(None),  # We will parse this from JSON
        languages: Optional[str] = Form(None),  # We will parse this from JSON
        driver_lic: Optional[str] = Form(None),  # We will parse this from JSON
        skills: Optional[str] = Form(None),  # We will parse this from JSON
        add_inf: Optional[str] = Form(None),
        avatar_file: UploadFile = File(None),
        avatar_url: Optional[str] = Form(None),
        template_image: int = Form(...)
):
    import json
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
            return {"error": "Формат файла должен быть PNG или JPEG"}
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