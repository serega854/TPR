# -*- coding: utf-8 -*-
from .Types import DataType
from abc import ABC, abstractmethod
import json


class DataReader(ABC):

    @abstractmethod
    def read(self) -> DataType:
        pass

class JSONDataReader (DataReader):
    def read(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
