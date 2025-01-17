import pickle
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    return max((len(group.students) for group in groups), default=0)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> list[Group]:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)

        unique_specialty = set()
        unique_groups_by_specialty_list = []

        for group in groups:
            if group.specialty.name not in unique_specialty:
                unique_specialty.add(group.specialty.name)
                unique_groups_by_specialty_list.append(group.specialty.name)
        return unique_groups_by_specialty_list


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
        return students
