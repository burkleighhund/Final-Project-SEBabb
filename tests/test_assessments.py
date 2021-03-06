import pytest
from music.assessment import Instructor
from music.assessment import Student


@pytest.fixture
def allowed_parameters():
    instruments = ["Tuba", "Flute", "Oboe"]
    return instruments


def test_instructor_instrument_validation(allowed_parameters):
    # arrange, act
    teacher = Instructor("John", "Doe", "Band", "Tuba")

    # assert
    assert teacher.instrument in allowed_parameters

#can use repository to really refine this testing
def given_parameters():
    grade = ["Middle School", "High School", "College"]
    return grade 

def test_can_create_student(given_parameters):
    kid = Student("James", "Smith", "Middle School", "Choir", "Tenor")

    assert kid.grade in given_parameters
    