"""
Author: Vo Viet Thanh
Date: 21/10/2021
Program: Write the code for a filtering that generates a list of the positive numbers in a list
named numbers. You should use a lambda to create the auxiliary function
Solution:
    ....
"""
numbers = [34, 1, 0, -23, 12, -88, 69, 107,90]
print("Original numbers in the list: ",numbers)
print("Positive numbers in the said list: ")
for pos_nums in numbers:
   if pos_nums > 0:
      print(pos_nums, end = " ")