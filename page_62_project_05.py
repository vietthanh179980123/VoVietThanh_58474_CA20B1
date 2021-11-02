"""
Author: Võ Viết Thanh
Date: 04/09/2021
Program: An object’s momentum is its mass multiplied by its velocity. Write a program
that accepts an object’s mass (in kilograms) and velocity (in meters per second) as
inputs and then outputs its momentum
Solution:
    1. Analys
    - Calcaculate an object’s momentum
    2. Inputs
    - An object’s mass (in kilograms)
    - Velocity (in meters per second)
    3. Outputs
    - Momentum
    4. Design
    - Input an object’s mass and velocity
    - The formulas are:
    + momentum = object*velocity
  ....
"""
# Request the inputs
object=int(input("Nhap khoi luong (kg): " ))
velocity=int(input("Nhap van toc cua vat (m/s): " ))
# Compute the momentum
momentum=object*velocity
# Display the momentum
print("Dong luong cua mot vat la: ",momentum)

