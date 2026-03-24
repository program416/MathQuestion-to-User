import sympy
import fractions
import math
class tier:
    def __init__(self, name, needScore, needLesson=20):
        self.name = name
        self.needScore = needScore
        self.needLesson = needLesson
    def __lt__(self, other):
        return self.needScore < other.needScore
    def __le__(self, other):
        return self.needScore <= other.needScore
    def __eq__(self, other):
        return self.needScore == other.needScore