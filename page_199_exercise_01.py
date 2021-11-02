"""
Author: Vo Viet Thanh
Date: 21/10/2021
Program: Write the code for a mapping that generates a list of the absolute values of the numbers in a list named numbers.
Solution:
    ....
"""

numbers = [5, -6, 7, -8, -10]
print("The original list is : " + str(numbers))
res = list(map(abs, numbers))
print("Absolute value list : " + str(res))