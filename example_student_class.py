"""
    Name: Võ Viết Thanh
    Date: 30/10/2021
    File: example_student_class.py
    Resources to manage a student's name and test scores
"""
from functools import reduce

class Student(object):
    def __init__(self, name, number):
        self._name = name
        self._scores = []
        for count in range(number):
            self._scores.append(0)

    def getname(self):
        return self._name

    def getscores(self):
        return self._scores

    def setscore(self,i,score):
        self._scores[i-1] = score

    def getscore(self,i):
        return self._scores[i-1]

    def getaverage(self):
        sum = reduce(lambda x, y: x+y, self._scores)
        return sum/len(self._scores)

    def gethighscore(self):
        return max(self._scores)
    def __str__(self):
        return "Name: " + self._name + "\nScores: " + \
            " ".join(map(str, self._scores))



