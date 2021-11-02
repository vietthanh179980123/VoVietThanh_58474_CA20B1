"""
Author: Vo Viet Thanh
Date: 8/10/2021
Program: Write a loop that replaces each number in a list named data with its absolute value.
Solution:
    ....
"""
data=[-2,-3,-6,-10,5,10]
processed = []
for number in data:
    if number < 0:
        processed.append(abs(number))
    else:
        processed.append(number)
print("Original numbers:\n", data)
print("Processed numbers:\n", processed)

