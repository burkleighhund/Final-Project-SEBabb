class Instructor:
    def __init__(self, fname, lname, teaches, instrument):
        self.fname = fname
        self.lname = lname
        self.teaches = teaches
        self.instrument = instrument
    
    def __str__(self) -> str:
        output = "The instructor's name is: " + self.fname + " " + self.lname
        output += "They teach: " + self.teaches
        output += "They specialize in: "+ self.instrument

       

class Student:
    def __init__(self, fname, lname, grade, dicipline, instrument):
        self.fname = fname
        self.lname = lname
        self.grade = grade
        self.dicipline = dicipline
        self.instrument = instrument
    
    def get_student(self):
        fullName = self.fname + " " + self.lname
        output = "The student's name is:" + self.fname + " " + self.lname
        output += "They are in:" + self.grade
        output += "They are currently enrolled in:" + self.dicipline
        output += "They specialize in:" +self.instrument




