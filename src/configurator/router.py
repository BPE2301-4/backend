# import external libraries
import asyncio

from . import create_pdf
from ..core import Resume, Employment, Schedule, Avatar, Name, WorkExp, Education, Languages, Skills, DriverLicense, work_exp_scheme
from fastapi import Form, File, UploadFile, APIRouter
from typing import Optional, List, Annotated
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
        surname: Annotated[str, Form(..., example='Антонов')],
        name: str = Form(..., example='Антон'),
        patronymic: Optional[str] = Form(None, example='Антонович'),
        phone: str = Form(default='8-800-555-35-35', min_length=11, max_length=16),
        email: EmailStr = Form(default='example@example.com'),
        work_exp: Optional[List[WorkExp]] = work_exp_scheme,
        birth_date: Optional[date] = Form(format="%Y-%m-%d"),
        city: Optional[str] = Form(None),
        citizenship: Optional[str] = Form(None),
        post: Optional[str] = Form(default='Мерчендайзер'),
        salary: Optional[str] = Form(default='40000 руб.'),
        employment: Optional[Employment] = Form(
            examples=[Employment.full, Employment.project, Employment.partial, Employment.intership,
                      Employment.volunteering]),
        schedule: Optional[Schedule] = Form(
            examples=[Schedule.full, Schedule.shift, Schedule.watch, Schedule.remote, Schedule.flexible]),
        education: Optional[List[Education]] = Form(...),
        languages: Optional[List[Languages]] = Form(...),
        driver_lic: Optional[List[DriverLicense]] = Form(...),
        skills: Optional[list[Skills]] = Form(...),
        add_inf: Optional[str] = Form(...),
        avatar_file: UploadFile = File(None),
        avatar_url: Optional[str] = Form(None),
        template_image: int = Form(...)
):
    resume = Resume(
        name=Name(surname=surname, name=name, patronymic=patronymic),
        phone=phone,
        email=email,
        work_exp=work_exp,
        birth_date=birth_date,
        city=city,
        citizenship=citizenship,
        post=post,
        salary=salary,
        employment=employment,
        schedule=schedule,
        education=education,
        languages=languages,
        driver_lic=driver_lic,
        skills=skills,
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
