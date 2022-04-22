import string
import py
from pytest import Session
import sqlalchemy as db
from unittest import result
from assessment import Instructor, Student
from sqlalchemy_utils import database_exists, create_database
import logging
from typing import Text
from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    insert
)

from sqlalchemy.orm import mapper

logger = logging.getLogger(__name__)


from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = db.create_engine('sqlite:///musicallessons.db', echo = True)
connection=engine.connect()
meta = MetaData()


def start_mappers():
    logger.info("string mappers")
    music_learners = mapper(Student, Student)
    music_teachers = mapper(Instructor, Instructor)

Student=Table(
    'Student', meta,
    Column('Id', Integer, primary_key = True),
    Column('Fname', String),
    Column('Lname', String),
    Column('Grade', String),
    Column('Discipline', String),
    Column('Instrument', String)
    )
    
Instructor=Table(
    'Instructor', meta,
    Column('Id', Integer, primary_key = True),
    Column('Fname', String),
    Column('Lname', String),
    Column('Teaches', String),
    Column('Discipline', String)
    )

def main ():
    meta.create_all(engine)

    while True:
        print("Is this a student or instructor? \n Enter done to exit:")
        question = str(input().lower())
        if(question == "student"):
            print("student id:")
            id = int(input())
            print("First name:")
            fname = str(input())
            print("Last name:")
            lname = str(input())
            print("What grade is the student in?:")
            grade = str(input())
            print("Are they in Band, Choir, or Orchestra?")
            discipline = str(input())
            print("What is the student's instrument/voice classification?")
            instrument = str(input())
            ins=insert(Student).values(Id=id, Fname=fname, Lname=lname, Grade=grade, Discipline=discipline, Instrument=instrument)
            conn=engine.connect()
            result=conn.execute(ins)
        

        elif(question == "instructor"):
            print("instructor id:")
            id = int(input())
            print("First name:")
            fname = str(input())
            print("Last name:")
            lname = str(input())
            print("What does the instructor teach? (Band, Choir, Orchestra)")
            teaches= str(input())
            print("What is their specialty?")
            dicipline = str(input())
            ins=insert(Instructor).values(Id=id, Fname=fname, Lname=lname, Teaches=teaches, Discipline=discipline)
            conn=engine.connect()
            result=conn.execute(ins)
        
        else: break
        
    for obj in Instructor:
        obj.get_instructor()

    for obj in Student:
        obj.get_student()
  
if __name__ == '__main__':
    main()
