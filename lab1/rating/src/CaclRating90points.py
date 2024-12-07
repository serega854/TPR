import json
from .Types import DataType
from .DataReader import DataReader

class CaclRating90points:
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
