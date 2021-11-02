"""
Author: Võ Viết Thanh
Date: 04/09/2021
Program: Write a program that takes the radius of a sphere (a floating-point number) as
input and then outputs the sphere’s diameter, circumference, surface area, and
volume.
Solution:
    1. Analys
    - Calcaculate the sphere’s diameter, circumference, surface area, and volume
    2. Inputs
    - The radius of a sphere
    3. Outputs
    - The sphere’s diameter
    - The sphere's circumference
    - The sphere's volume
    - The sphere's surface area
    4. Design
    - Input the radius of a sphere
    - The formulas are:
    + spdiameter = radius*2
    + spcircumference = 2*pi*radius
    + spvolume = 4/3*(pi*(radius**3))
    + spsurfacearea = 4*pi*(radius**2)
  ....
"""
# Initialize the constants
pi = 3.14
# Request the input
radius = float(input("Nhap ban kinh hinh cau: "))
# Compute the sphere's diameter, circumference, surface area, and volume
spdiameter = radius*2
spcircumference = 2*pi*radius
spvolume = 4/3*pi*(radius**3)
spsurfacearea = 4*pi*(radius**2)
# Display the sphere's diameter, circumference, surface area, and volume
print("Duong kinh cua hinh cau la: ",spdiameter)
print("Chu vi cua hinh cau la: ",spcircumference)
print("The tich cua hinh cau la: ",spvolume)
print("Dien tich cua hinh cau la: ",spsurfacearea)
