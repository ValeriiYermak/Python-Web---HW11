from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class Base(DeclarativeBase):
    pass


class Contact(Base):
    __tablename__ = "contacts"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), index=True)
    lastname: Mapped[str] = mapped_column(String(50), index=True)
    email: Mapped[str] = mapped_column(String(50), index=True)
    phone: Mapped[str] = mapped_column(String(50))
    birthdate: Mapped[str] = mapped_column()
    others_info: Mapped[str] = mapped_column(String(250))
    completed: Mapped[bool] = mapped_column(default=False)
