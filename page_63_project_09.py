"""
Author: Võ Viết Thanh
Date: 05/09/2021
Program: Write a program that takes as input a number of kilometers and prints the corresponding number of nautical miles. Use the following approximations:
• A kilometer represents 1/10,000 of the distance between the North Pole and
the equator.
• There are 90 degrees, containing 60 minutes of arc each, between the North
Pole and the equator.
• A nautical mile is 1 minute of an arc
Solution:
    1. Analys
    - Calcaculate a number of kilometers and prints the corresponding number of nautical miles
    2. Inputs
    - A number of kilometers
    3. Outputs
    - Nautical
    4. Design
    - Input a number of kilometers
    - The formulas are:
    + A light year = The distance a light * light travel
  ....
"""
# Request the input
kilometer=float(input("Nhap so (km) :"))
# Compute the nautical
nauts=kilometer*90*60/10000.0
# Display the number of minute of a year
print("Hai ly la: ",nauts)
