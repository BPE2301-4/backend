# import sqlalchemy libraries
from sqlalchemy.orm import mapped_column, Mapped
# import from folder 'src/core/models/'
from .base import Base


class Url(Base):
    __tablename__ = 'url'

    id: Mapped[int] = mapped_column(primary_key=True,
                                    nullable=False,
                                    autoincrement=True,
                                    unique=True)
    url: Mapped[str] = mapped_column(nullable=False)
