# import external libraries
from enum import Enum
from pydantic import BaseModel, Field, EmailStr
import datetime


class Enployment(Enum):
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
    name: str = 'Антонов Антон Антонович'
    phone: str = Field(min_length=11, max_length=16, default='8-800-555-35-35')
    email: EmailStr = Field(default='example@example.com')
    work_exp: str = Field(default='Отсутствует')  # поменять на строку или переработать
    birth_date: datetime.date = Field(default=datetime.date(2000, 1, 1))  # поменять на дату рождения
    city: str = Field(default='Москва')
    citizenship: str = Field(default='РФ')
    post: str = Field(default='Мерчендайзер')
    salary: str = Field(default='40000 руб.')
    enployment: Enployment = Enployment.full
    schedule: Schedule = Schedule.full
    education: str = Field(default='Среднее полное')  # поменять на строку или доработать
    about: str = ''

    def configue_prompt(self):
        return f'Создай резюме по следующим параметрам:\
    1) Имя: {self.name}\
    2) Телефон: {self.phone}\
    3) Email: {self.email}\
    4) Опыт работы: {self.work_exp}\
    5) Дата рождения: {str(self.birth_date)}\
    6) Город проживания: {self.city}\
    7) Гражданство: {self.citizenship}\
    8) Должность: {self.post}\
    9) Желаемая заработная плата: {self.salary}\
    10) График работы: {self.schedule}\
    11) Образование: {self.education}\
    12) Занятость: {self.enployment}\
    13) О себе: {self.about}\
    \
    Если в некоторых полях нет информации , то они будут заполнены восклицательным знаком.\
    Сделай резюме максимально привлекательным для работодателя и оформи его так , \
    чтобы я смог скопировать текст без правок и изменений. \
    Дата рождения ( поле 5 ) будет представленно в формате YYYY-MM-DD \
    Так же более точно и с пояснениями оформи пункт 4 , добавив туда названия полей для различной информации , \
    пункт 11  так же оформи более точно , с добавлением полей для разграничения информации , \
    а пункт 13 дополни соответствующими для профессии , указанной в пункте 8 , навыками.'
