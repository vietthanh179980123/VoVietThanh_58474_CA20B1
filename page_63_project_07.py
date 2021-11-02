"""
Author: Võ Viết Thanh
Date: 04/09/2021
Program: Write a program that calculates and prints the number of minutes in a year.
Solution:
    1. Analys
    - Calcaculate and prints the number of minutes in a year
    2. Inputs
    - year
    3. Outputs
    - Momentum
    4. Design
    - Input the object’s mass and velocity
    - The formulas are:
    + the object’s kinetic energy = 1/2 * the object's mass * (velocity**2)
  ....
"""
# Request the input
dayinyear=int(input("Nhap so ngay trong 1 nam: "))
# Compute the number of minute of a year
number=dayinyear*(24*60)
# Display the number of minute of a year
print("So phut trong 1 nam la: ",number)
