# import external libraries
from enum import Enum
from pydantic import BaseModel, Field, EmailStr


class Enployment(Enum):
    full = 'full'  # полная занятость
    partial = 'partial'  # частичная занятость
    project = 'project'  # проектная работа/разовое задание
    volunteering = 'volunteering'  # волонтерство
    intership = 'intership'  # стажировка


class Schedule(Enum):
    full = 'full'  # полный график
    shift = 'shift'  # сменный график
    flexible = 'flexible'  # гибкий график
    remote = 'remote'  # удаленная работа
    watch = 'watch'  # вахтовый метод


class Education(Enum):
    secondary = 'secondary'  # среднее
    secondary_special = 'secondary special'  # среднее специальноее
    incomplete_higher = 'incomplete higher'  # незаконченное высшее
    bachelor = 'bachelor'  # бакалавр
    master = 'master'  # магистр
    higher = 'higher'  # высшее
    candidate = 'candidate'  # кандидат наук
    doctor = 'doctor'  # доктор наук


class Resume(BaseModel):
    name: str = 'Антонов Антон Антонович'
    phone: str = Field(min_length=11, max_length=16, default='8-800-555-35-35')
    email: EmailStr = Field(default='example@example.com')
    work_exp: int = Field(ge=0, default='0')
    age: int = Field(ge=18, default='18')
    enployment: Enployment = Enployment.full
    schedule: Schedule = Schedule.full
    education: Education = Education.bachelor
    languages: str = 'Russian English'
    about: str
