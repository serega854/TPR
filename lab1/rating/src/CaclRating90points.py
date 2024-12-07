import json
from .Types import DataType
from .DataReader import DataReader


class CaclRating90points:
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