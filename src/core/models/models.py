# import sqlalchemy libraries
from sqlalchemy.orm import mapped_column, Mapped
# import from folder 'src/core/models/'
from base import Base
# import from folder 'src/core/'
from ..schemas import Enployment, Schedule


class Resume(Base):
    __tablename__ = 'resume'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False,
                                      default='Антонов Антон Антонович')
    phone: Mapped[str] = mapped_column(nullable=False,
                                       default='8-800-555-35-35')
    email: Mapped[str] = mapped_column(nullable=False,
                                       default='example@example.com')
    work_exp: Mapped[str] = mapped_column(nullable=False,
                                          default='Отсутствует')
    birth_date: Mapped[int] = mapped_column(nullable=False,
                                            default=18)
    city: Mapped[str] = mapped_column(nullable=False,
                                      default='Москва')
    citizenship: Mapped[str] = mapped_column(nullable=False,
                                             default='РФ')
    post: Mapped[str] = mapped_column(nullable=False,
                                      default='Мерчендайзер')
    salary: Mapped[str] = mapped_column(nullable=False,
                                        default='40000')
    enployment: Mapped[Enployment]
    schedule: Mapped[Schedule]
    education: Mapped[str] = mapped_column(nullable='False',
                                           default='Среднее полное')
    about: Mapped[str] = mapped_column(nullable=True,
                                       default='Ничего')
