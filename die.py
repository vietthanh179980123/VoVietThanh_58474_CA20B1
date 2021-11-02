"""
    Name: Võ Viết Thanh
    Date:30/10/2021
    File: die.py
    This module defines the Die class.
"""
from random import randint
class Die(object):

    def __init__(self):
        self.value = 1

    def roll(self):
        self.value = randint(1, 6)

    def getvalue(self):
        return self.value

    def __str__(self):
        return str(self.value)