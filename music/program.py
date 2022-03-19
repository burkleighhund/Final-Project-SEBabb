from assessment import Instructor, Student

def main ():

    student=[]
    instructor=[]

    while True:
        print("Is this a student or instructor? \n Enter done to exit:")
        question = str(input().lower())
        if(question == "student"):
            print("First name:")
            fname = str(input())
            print("Last name:")
            lname = str(input())
            print("What grade is the student in?:")
            grade = str(input())
            print("Are they in Band, Choir, or Orchestra?")
            dicipline = str(input())
            print("What is the student's instrument/voice classification?")
            instrument = str(input())
            s1 = Student(fname,lname,grade,dicipline,instrument)
            student.append(s1)
        
        elif(question == "instructor"):
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
        
        else: break
        
    for obj in instructor:
        obj.get_instructor()

    for obj in student:
        obj.get_student()
  
if __name__ == '__main__':
    main()
