# -*- coding: utf-8 -*-
from .Types import DataType

RatingType = dict[str, float]


class CalcRating_90_studets:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.rating: RatingType = {}

    def calc_90_rating(self) -> RatingType:
        key_answer
        for key in self.data:
            count = 0
            self.rating[key] = 0.0
            for subject in self.data[key]: 
                self.rating[key] += subject[1]
                if self.rating[key] >= 90:
                  count++
                if count >= 2:
                  key_answer = key
                  
        return key_answer
        
