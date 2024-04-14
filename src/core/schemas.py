# import external libraries
from enum import Enum
from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from fastapi import UploadFile
import datetime


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


class Resume(BaseModel):
    avatar: Optional[UploadFile] = None
    name: str = 'Антонов Антон Антонович'
    phone: str = Field(min_length=11, max_length=16, default='8-800-555-35-35')
    email: EmailStr = Field(default='example@example.com')
    work_exp: str = Field(default='Отсутствует')
    birth_date: datetime.date = Field(default=datetime.date(2000, 1, 1))
    city: Optional[str] = Field(default='Москва')
    citizenship: Optional[str] = Field(default='РФ')
    post: str = Field(default='Мерчендайзер')
    salary: str = Field(default='40000 руб.')
    employment: Employment = Employment.full
    schedule: Schedule = Schedule.full
    education: str = Field(default='Среднее полное')
    about: Optional[str] = ''
