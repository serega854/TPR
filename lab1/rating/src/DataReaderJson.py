<<<<<<< HEAD
import json
from .Types import DataType
from .DataReader import DataReader


class JsonDataReader(DataReader):
    
=======
from .Types import DataType
from .DataReader import DataReader
import json


class DataReaderJson(DataReader):

>>>>>>> ffb51f52bae29ca439e4d3beef6fd6f35df5849b
    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            data = json.load(file)
            students: DataType = {}
            for student_name, subjects in data.items():
                students[student_name] = [(subject, score) for
                                          subject, score in subjects.items()]
<<<<<<< HEAD
            return students
=======
            return students
>>>>>>> ffb51f52bae29ca439e4d3beef6fd6f35df5849b
