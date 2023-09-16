from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped

from database import Base


class Source(Base):
    __tablename__ = "sources"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    name: Mapped[str] = mapped_column(String, index=True)
    abbr: Mapped[str] = mapped_column(String, index=True)


class Class(Base):
    __tablename__ = "classes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    name: Mapped[str] = mapped_column(String, index=True)
    abbr: Mapped[str] = mapped_column(String, index=True)
