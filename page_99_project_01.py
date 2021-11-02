"""
Author: Võ Viết Thanh
Date: 17/09/2021
Program: Write a program that accepts the lengths of three sides of a triangle as inputs.
The program output should indicate whether or not the triangle is an equilateral
triangle.
Solution:
  ....
"""
x=int(input("Nhap do danh canh thu 1: "))
y=int(input("Nhap do dai canh thu 2: "))
z=int(input("Nhap do dai canh thu 3: "))
if x==y==z:
    print("Day la tam giac deu")
else:
    print("Day khong phai la tam giac deu")
