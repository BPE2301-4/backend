# import sqlalchemy libraries
from sqlalchemy import Column, Integer, String, ARRAY, MetaData, JSON, Enum
from sqlalchemy.orm import mapped_column, Mapped
# import from folder 'src' via __init__
from .. import Base
# import from actual folder
from .schemas import Education, Enployment, Schedule

metadata = MetaData()


class Resume(Base):
    __tablename__ = 'resume'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False,
                                      default='Антонов Антон Антонович')
    phone: Mapped[str] = mapped_column(nullable=False,
                                       default='8-800-555-35-35')
    email: Mapped[str] = mapped_column(nullable=False,
                                       default='example@example.com')
    work_exp: Mapped[int] = mapped_column(nullable=False,
                                          default=0)
    age: Mapped[int] = mapped_column(nullable=False,
                                     default=18)
    enployment: Mapped[Enployment]
    schedule: Mapped[Schedule]
    education: Mapped[Education]
    languages: Mapped[str] = mapped_column(nullable=False,
                                           default='Russian English')
    about: Mapped[str] = mapped_column(nullable=True,
                                       default='Ничего')
