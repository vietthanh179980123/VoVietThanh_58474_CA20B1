"""
Author: Võ Viết Thanh
Date: 04/09/2021
Program: Light travels at 3 *10^8 meters per second. A light-year is the distance a light beam
travels in one year. Write a program that calculates and displays the value of a
light-year.
Solution:
    1. Analys
    - Calcaculate and displays the value of a light-year.
    2. Outputs
    - Year
    3. Design
    - Initialize the constants
    + Light travels
    + Year
    - The formulas are:
    + A light year = The distance a light * light travel
  ....
"""
# Initialize the constants
lighttravels=3*(10**8)
year=365*24*60*60
# Compute the number of minute of a year
lightyear=lighttravels*year
# Display the number of minute of a year
print("Nam anh sang la: ",lightyear,"meter in a year")
