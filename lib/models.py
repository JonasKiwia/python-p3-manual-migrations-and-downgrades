import os
import sys

sys.path.append(os.getcwd())


from datetime import datetime

from sqlalchemy import create_engine, desc
from sqlalchemy import (CheckConstraint, UniqueConstraint,
    Column, DateTime, Integer, String)

from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///migrations_test.db')

Base = declarative_base()

# models.py (After change)

class Student(Base):
    __tablename__ = 'students'
    __table_args__ = (
        UniqueConstraint('email', name='unique_email'),
        CheckConstraint('grade BETWEEN 1 AND 12', name='grade_between_1_and_12')
    )

    id = Column(Integer(), primary_key=True)
    full_name = Column(String(), index=True)  # Renamed from 'name'
    email = Column(String(55))
    grade = Column(Integer())
    birthday = Column(DateTime())
    enrolled_date = Column(DateTime(), default=datetime.now())

