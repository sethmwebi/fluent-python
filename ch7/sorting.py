# student_tuples = [("john", "A", 15), ("jane", "B", 12), ("dave", "B", 10)]
# print(sorted(student_tuples, key=lambda student: student[2]))
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))


student_objects = [
    Student("john", "A", 15),
    Student("jane", "B", 12),
    Student("dave", "B", 10),
]

# print(sorted(student_objects, key=lambda student: student.age))
from operator import attrgetter, itemgetter

student_tuples = [
    ("john", "A", 15),
    ("jane", "B", 12),
    ("dave", "B", 10),
]
# print(sorted(student_tuples, key=itemgetter(1, 2)))
# print(sorted(student_objects, key=attrgetter("grade", "age")))
from functools import partial
from unicodedata import normalize

names = "Zoë Åbjørn Núñez Élana Zeke Abe Nubia Eloise".split()


# print(sorted(names, key=partial(normalize, "NFC")))
# print(sorted(student_tuples, key=itemgetter(2), reverse=True))
# print(sorted(student_objects, key=attrgetter("age"), reverse=True))
# s = sorted(student_objects, key=attrgetter("age"))
# print(sorted(s, key=attrgetter("grade"), reverse=True))
def multisort(xs, specs):
    for key, reverse in reversed(specs):
        xs.sort(key=attrgetter(key), reverse=reverse)
    return xs


# print(multisort(list(student_objects), (("grade", True), ("age", False))))
decorated = [(student.grade, i, student) for i, student in enumerate(student_objects)]
decorated.sort()
# print([student for grade, i, student in decorated])
Student.__lt__ = lambda self, other: self.age < other.age
print(sorted(student_objects))
