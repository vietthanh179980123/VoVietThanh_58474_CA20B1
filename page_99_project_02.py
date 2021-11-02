"""
Author: Võ Viết Thanh
Date: 17/09/2021
Program: Write a program that accepts the lengths of three sides of a triangle as inputs.
The program output should indicate whether or not the triangle is a right triangle. Recall from the Pythagorean theorem that in a right triangle, the square of
one side equals the sum of the squares of the other two sides
Solution:
  ....
"""

x=float(input("Nhap do danh canh goc vuong 1: "))
y=float(input("Nhap do dai canh goc vuong 2: "))
z=float(input("Nhap do dai canh huyen: "))
if z**2 == x**2 + y**2 or y**2 == z**2 - x**2 or x**2 == z**2 - y**2:
    print("Day la tam giac vuong")
else:
    print("Day khong phai la tam giac vuong")
