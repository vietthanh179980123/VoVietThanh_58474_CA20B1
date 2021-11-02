"""
Author: Võ Viết Thanh
Date: 15/09/2021
Program: Write a format operation that builds a string for the float variable amount that has
exactly two digits of precision and a field width of zero.
Solution:

  ....
"""
amount = float(input("Nhap so vao day: "))
print("%0.2f" % amount)

