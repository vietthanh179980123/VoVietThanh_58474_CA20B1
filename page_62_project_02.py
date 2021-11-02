"""
Author: Võ Viết Thanh
Date: 04/09/2021
Program: You can calculate the surface area of a cube if you know the length of an edge.
Write a program that takes the length of an edge (an integer) as input and prints
the cube’s surface area as output.
Solution:
    1. Analys
    - Calcaculate the surface area of a cube
    2. Inputs
    - length
    3. Outputs
    - the surface area of a cube
    4. Design
    - Input the length of an edge then use the formula to calculate the area. The formula is area = 6*(length**2)
  ....
"""
# Request the inputs
length = int(input("Nhap chieu dai canh cua khoi lap phuong: "))
# Compute the surface area of the cube
area = 6*(length**2)
# Display the surface area of the cube
print("Dien tich be mat cua khoi lap phuong la: ", area)
