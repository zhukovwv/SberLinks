"""
SQL Alchemy models declaration.
https://docs.sqlalchemy.org/en/14/orm/declarative_styles.html#example-two-dataclasses-with-declarative-table
Dataclass style for powerful autocompletion support.

https://alembic.sqlalchemy.org/en/latest/tutorial.html
Note, it is used by alembic migrations logic, see `alembic/env.py`

Alembic shortcuts:
# create migration
alembic revision --autogenerate -m "migration_name"

# apply all migrations
alembic upgrade head
"""

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    pass


class Link(Base):
    __tablename__ = 'links'

    id = Column(Integer, primary_key=True)
    url = Column(String(255), nullable=False)
    time_visited = Column(Integer, nullable=False)
