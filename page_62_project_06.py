"""
Author: Võ Viết Thanh
Date: 04/09/2021
Program: The kinetic energy of a moving object is given by the formula KE=(1/2)mv^2
where m is the object’s mass and v is its velocity. Modify the program you created
in Project 5 so that it prints the object’s kinetic energy as well as its momentum
Solution:
    1. Analys
    - Calcaculate the object’s kinetic energy as well as its momentum
    2. Inputs
    - The object’s mass
    - Velocity (in meters per second)
    3. Outputs
    - Momentum
    4. Design
    - Input the object’s mass and velocity
    - The formulas are:
    + the object’s kinetic energy = 1/2 * the object's mass * (velocity**2)
  ....
"""
# Request the inputs
object=int(input("Nhap khoi luong: "))
velocity=int(input("Nhap van toc cua vat: "))
# Compute the object’s kinetic energy
kinetic=1/2*object*(velocity**2)
# Display the object’s kinetic energy
print("Dong luong cua mot vat la: ",kinetic)
