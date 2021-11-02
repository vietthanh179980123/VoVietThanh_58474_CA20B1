"""
Author: Vo Viet Thanh
Date: 8/10/2021
Program: Assume that data refers to a list of numbers, and result refers to an empty list.
Write a loop that adds the nonzero values in data to the result list, keeping them
in their relative positions and excluding the zeros.
Solution:
    ....
"""
data = [35,90,67,89,102]
result = ""
for number in data:
   if number != 0:
       result += str(number)
