import string
from unittest import result
from assessment import Instructor, Student
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine
engine = create_engine('sqlite:///musicallessons.db', echo = True)

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///musicallessons.db', echo = True)
meta = MetaData()
Students=Table(
    'Students', meta,
    Column('Id', Integer, primary_key = True),
    Column('Fname', String),
    Column('Lname', String),
    Column('Grade', String),
    Column('Discipline', String),
    Column('Instrument', String)
    )
    
Instructors=Table(
    'Instructors', meta,
    Column('Id', Integer, primary_key = True),
    Column('Fname', String),
    Column('Lname', String),
    Column('Teaches', String),
    Column('Discipline', String)
    )

def main ():

    student=[]
    instructor=[]

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
            s1 = Student(fname,lname,grade,discipline,instrument)
            student.append(s1)
            ins=Students.insert().values(Id=id, Fname=fname, Lname=lname, Grade=grade, Discipline=discipline, Instrument=instrument)
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
            i1 = Instructor(fname,lname,teaches,dicipline)
        #   p1.get_instructor()
            instructor.append(i1)
            ins=Instructors.insert().values(Id=id, Fname=fname, Lname=lname, Teaches=teaches, Discipline=discipline)
            conn=engine.connect()
            result=conn.execute(ins)
        
        else: break
        
    for obj in instructor:
        obj.get_instructor()

    for obj in student:
        obj.get_student()
  
if __name__ == '__main__':
    main()
