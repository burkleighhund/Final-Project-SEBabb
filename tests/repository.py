# making use of type hints: https://docs.python.org/3/library/typing.html
from lib2to3.pytree import Base
from typing import List, Set
import py
from assessment import Student, Instructor
from abc import ABC, abstractmethod
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker




class AbstractRepository(ABC):
    def __init__(self):
        self.seen = set()

#     def add(self, student: Student):
#         self._add(student)

#     def add(self, instructor: Instructor):
#         self._add(instructor)

#     def get(self, title: str):
#         bookmark = self._get(title)

#         if bookmark:
#             self.seen.add(bookmark)

#         return bookmark

#   #  @abstractmethod
#     def _add(self, student: Student):
#         raise NotImplementedError

#     @abstractmethod
#     def _add(self, instructor: Instructor):
#         raise NotImplementedError

#     @abstractmethod
#     def _get(self, title) -> Bookmark:
#         raise NotImplementedError

#     @abstractmethod
#     def _edit(self, bookmark: Bookmark):
#         found = self.get(bookmark.title)
#         if found:
#             pass

    @abstractmethod
    def add_one_student(student: Student) -> int:
        raise NotImplementedError("Derived classes must implement add_one")

    @abstractmethod
    def add_many_students(student: Student) -> int:
        raise NotImplementedError("Derived classes must implement add_many")

    @abstractmethod
    def delete_one_student(student) -> int:
        raise NotImplementedError("Derived classes must implement delete_one")

    @abstractmethod
    def delete_many_students(student) -> int:
        raise NotImplementedError("Derived classes must implement delete_many")

    @abstractmethod
    def update_student(student) -> int:
        raise NotImplementedError("Derived classes must implement update")

    @abstractmethod
    def update_many_students(student) -> int:
        raise NotImplementedError("Derived classes must implement update_many")

    @abstractmethod
    def find_first_student(query) -> Student:
        raise NotImplementedError("Derived classes must implement find_first")

    @abstractmethod
    def find_all_students(query) -> list[Student]:
        raise NotImplementedError("Derived classes must implement find_all")

    @abstractmethod
    def add_one_instructor(instructor: Instructor) -> int:
        raise NotImplementedError("Derived classes must implement add_one")

    @abstractmethod
    def add_many_instructors(instructor: Instructor) -> int:
        raise NotImplementedError("Derived classes must implement add_many")

    @abstractmethod
    def delete_one_instructor(instructor) -> int:
        raise NotImplementedError("Derived classes must implement delete_one")

    @abstractmethod
    def delete_many_instructors(instructor) -> int:
        raise NotImplementedError("Derived classes must implement delete_many")

    @abstractmethod
    def update_instructor(instructor) -> int:
        raise NotImplementedError("Derived classes must implement update")

    @abstractmethod
    def update_many_instructors(instructor) -> int:
        raise NotImplementedError("Derived classes must implement update_many")

    @abstractmethod
    def find_first_instructor(query) -> Instructor:
        raise NotImplementedError("Derived classes must implement find_first")

    @abstractmethod
    def find_all_instructors(query) -> list[Instructor]:
        raise NotImplementedError("Derived classes must implement find_all")


class SqlAlchemyRepository(AbstractRepository):
    """
    Uses guidance from the basic SQLAlchemy 1.3 tutorial: https://docs.sqlalchemy.org/en/13/orm/tutorial.html
    """

    def __init__(self, url=None) -> None:
        super().__init__()

        self.engine = None
        Base= declarative_base


        # create db connection
        if url != None:
            self.engine = create_engine(url)
        else:
            # let's default to in-memory for now
            self.engine = create_engine("sqlite:///:memory:", echo=True)

        # ensure tables are there
        Base.metadata.create_all(self.engine)

        # obtain session
        # the session is used for all transactions
        self.Session = sessionmaker(bind=self.engine)

    def add_one(self, student: Student) -> int:
        self.Session.add(student)
        self.Session.commit()
        pass

    def add_many(self, student: list[Student]) -> int:
        self.Session.add(student)
        pass

    def delete_one(self, student) -> int:
        pass

    def delete_many(self, student) -> int:
        pass

    def update(self, student) -> int:
        pass

    def update_many(self, student) -> int:
        pass

    def find_first(self, query) -> Student:
        pass

    def find_all(self, query) -> list[Student]:
        pass

    def add_one_instructor(self, instructor: Instructor) -> int:
        self.Session.add(instructor)
        self.Session.commit()
        pass

    def add_many(self, instructor: list[Instructor]) -> int:
        self.Session.add(instructor)
        pass

    def delete_one(self, instructor) -> int:
        pass

    def delete_many(self, instructor) -> int:
        pass

    def update(self, instructor) -> int:
        pass

    def update_many(self, instructor) -> int:
        pass

    def find_first(self, query) -> Instructor:
        pass

    def find_all(self, query) -> list[Instructor]:
        pass