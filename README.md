# Final-Project-SEBabb

Music Lessons On Demand

*A former Music Teachers wish for a simpler and easier to access supplemental lessons guide

This project is meant to provide an easier, more affordable/accessible way to supplement music lessons across grade levels. Specifically, this program should let a student find the lessons they need based on instructor, instrument, and grade level. It should also allow instructors to post content based off of the same constraints.

The way to use this (for now) is terminal based, where it takes in user input in the form of Student/Instructor, First Name, Last Name, Grade, Instrument, and Group of choice (choir, band, orchestra), and then find pre-uploaded information based off of these selections.

The dependencies for this are import statements which are discussed below. The biggest one is that it relies on the Python Language and supporting packages.

*The Supporting Files/Constraints


    -**pytest**: This is a testing framework based on Python that is mainly used to write API test cases (This is the API portion of my project)

    -**SQLalchemy**: This is the Python SQL toolkit and object relational mapper I used in my project to help me utilize SQL without connecting straight to SQlite browser.

    -**python**: This one is self explanatory, but for those who aren't aware, Python is a high-level programming language with dynamic semantics.

    -**unittest**: This is a framework package inside of Python that makes my code future proof. Basically it helps me anticipate the cases where my code could fail or potentially produce a bug.

    -**AbstractMethod**, **ABC**: This is a method in python that is declared but contains no implementation. 

*This repository is made to be a smaller version of Dane's testing example.There is the following:

    #Layered Architecture

    At the base level, the architecture is designed with a layered effect which include these elements:
        -**Presentation**:(will be a module called music.py here)
        -**Business Logic Layer**: (will be a module called tests.py here)
        -**Presistence Layer**:(will be a module called program.py here)

Instead of connecting straight to an SQlite browser, I attempted to build a pseudo table inside a Virtual Environment. I focused mostly on the actual testing implementation though rather than the full program for this project.

Some of the constraints limit the type of information that can be input, as well as limiting what instruments/vocal parts can be chosen. However, this section can be expanded upon later once proper testing and construction on the true database are complete. 


*Assumptions Made:

**There were several assumptions made about this project:

    1)That the user would be either a Student or and Instructor in the music field (can also be an administrator/facilitator if there is no specified instructor).

    2)The user would be using this for the academic music field, not for any other subject.

    3)This program would be used only in a school or private lesson setting not in another setting (i.e. a bank or a hospital)

    4)The user would be inputting the proper information when prompted, not leaving options blank or putting in null characters (there is testing paramaters set up for this in the event that they do attempt one of the above, the program will just exit to the main screen).

    5)There will only be tables of the input material, not of random information.