import logging
from typing import Text
from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
)

from sqlalchemy.orm import mapper

logger = logging.getLogger(__name__)

metadata = MetaData()


Students=Table(
    'Students', metadata,
    Column('Id', Integer, primary_key = True),
    Column('Fname', String),
    Column('Lname', String),
    Column('Grade', String),
    Column('Discipline', String),
    Column('Instrument', String)
    )
    
Instructors=Table(
    'Instructors', metadata,
    Column('Id', Integer, primary_key = True),
    Column('Fname', String),
    Column('Lname', String),
    Column('Teaches', String),
    Column('Discipline', String)
    )


def start_mappers():
    logger.info("string mappers")
    music_learners = mapper(Students, Students)
    music_teachers = mapper(Instructors, Instructors)


