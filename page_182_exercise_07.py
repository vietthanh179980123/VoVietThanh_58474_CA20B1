"""
Author: Vo Viet Thanh
Date: 21/10/2021
Program: Explain what happens when the following recursive function is called with the
values "hello" and 0 as arguments:
    def example(aString, index):
        if index == len(aString):
            return ""
        else:
            return aString[index] + example(aString, index + 1)
Solution:
    ....
"""
def example(aString, index):
    if index == len(aString):
        return ""
    else:
        return aString[index] + example(aString, index + 1)
