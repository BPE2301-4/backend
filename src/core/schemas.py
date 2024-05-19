# import external libraries
from enum import Enum
from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import date
from PIL import ImageFont
from .resume_templates import font_path


class Font(Enum):
    bold_left = ImageFont.truetype(font_path.medium, 44)
    smpl_left = ImageFont.truetype(font_path.light, 38)
    bold_right = ImageFont.truetype(font_path.medium, 54)
    smpl_right = ImageFont.truetype(font_path.light, 48)
    name = ImageFont.truetype(font_path.bold, 80)


class Text(BaseModel):
    text: str
    text_padding: int
    text_font: Font


class Employment(Enum):
    full = 'Полная'  # полная занятость
    partial = 'Частичная'  # частичная занятость
    project = 'Проектная работа/разовое заданиее'  # проектная работа/разовое задание
    volunteering = 'Воллонтерство'  # волонтерство
    intership = 'Стажировка'  # стажировка


class Schedule(Enum):
    full = 'Полный'  # полный график
    shift = 'Сменный'  # сменный график
    flexible = 'Гибкий'  # гибкий график
    remote = 'Удаленная работа'  # удаленная работа
    watch = 'Вахтовый метод'  # вахтовый метод


class Avatar(BaseModel):
    file: Optional[bytes] = None
    url: Optional[str] = None


class EducationForm(Enum):
    full = 'Очно'
    part = 'Заочно'
    courses = 'Курсы'


class Education(BaseModel):
    place: str = 'МТУСИ'
    year_of_grad: int = 2024
    faculty: str = 'ИТ'
    speciality: str = 'Разработка и сопровождение ПО'
    education_for: EducationForm = EducationForm.full


class Name(BaseModel):
    surname: str = 'Антонов'
    name: str = 'Антон'
    patronymic: Optional[str]


class WorkExp(BaseModel):
    post: str
    start_date: date
    finish_date: date
    place: str
    resp_and_achiev: str


class Languages(BaseModel):
    lang: str
    lvl: str


class Skills(BaseModel):
    skill: str
    lvl: str


class DriverLicense(Enum):
    A = 'A'
    A1 = 'A1'
    B = 'B'
    B1 = 'B1'
    C = 'C'
    C1 = 'C1'
    D = 'D'
    D1 = 'D1'
    BE = 'BE'
    CE = 'CE'
    C1E = 'C1E'
    DE = 'DE'
    D1E = 'D1E'
    M = 'M'
    Tm = 'Tm'
    Tb = 'Tb'


class Resume(BaseModel):
    avatar: Optional[Avatar] = None
    name: Name
    phone: str = Field(min_length=11, max_length=16, default='8-800-555-35-35')
    email: EmailStr = Field(default='example@example.com')
    work_exp: Optional[List[WorkExp]]
    birth_date: Optional[date] = Field(default=date(2000, 1, 1))
    city: Optional[str] = Field(default='Москва')
    citizenship: Optional[str] = Field(default='РФ')
    post: Optional[str] = Field(default='Мерчендайзер')
    salary: Optional[str] = Field(default='40000 руб.')
    employment: Optional[Employment] = Employment.full
    schedule: Optional[Schedule] = Schedule.full
    education: Optional[List[Education]]
    languages: Optional[List[Languages]]
    driver_lic: Optional[List[DriverLicense]]
    skills: Optional[List[Skills]]
    add_inf: Optional[str]


class ResumeForTable(BaseModel):
    name: str = ''
    email: EmailStr = 'example@example.com'
    phone: str = ''
    work_exp: str = ''
    birth_date: date = date(2020, 10, 10)
    city: str = ''
    citizenship: str = ''
    post: str = ''
    salary: str = ''
    employment: Employment = Employment.full
    schedule: Schedule = Schedule.full
    education: str = ''
    about: str = ''