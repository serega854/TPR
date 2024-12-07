import json
from .Types import DataType
from .DataReader import DataReader


class CaclRating90points:
<<<<<<< HEAD
    def __init__(self, data: DataType):
        self.data = data

    def count_students_90_points(self) -> int:
        students_90_points = 0
        for students, subjects in self.data.items():
            for subject, score in subjects:
                if score > 90:
                    students_90_points += 1
                    break

        return students_90_points

    def print_result(self):
        students_90_points_answer = self.students_90_points()
        print(f"Количество студентов с задолженностями: {students_90_points_answer}")
=======

    def __init__(self, data: DataType):
        self.data = data

    def find_student_with_two_subjects_above_90(self):
        for student, subjects in self.data.items():
            count_above_90 = 0
            for subject, score in subjects:
                if score > 90:
                    count_above_90 += 1
                if count_above_90 >= 2:
                    return student

        return None

    def print_result(self):
        student = self.find_student_with_two_subjects_above_90()
        if student:
            print(f"Студент, имеющий более 90 баллов за 2 предмета: {student}")
        else:
            print("Студента, имеющего более 90 баллов за 2 предмета нет")
>>>>>>> ffb51f52bae29ca439e4d3beef6fd6f35df5849b
