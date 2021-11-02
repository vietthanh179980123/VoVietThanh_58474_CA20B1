"""
Author: Võ Viết Thanh
Date: 05/09/2021
Program: An employee’s total weekly pay equals the hourly wage multiplied by the total
number of regular hours plus any overtime pay. Overtime pay equals the total
overtime hours multiplied by 1.5 times the hourly wage. Write a program that
takes as inputs the hourly wage, total regular hours, and total overtime hours and
displays an employee’s total weekly pay
Solution:
    1. Analys
    - Displays an employee’s total weekly pay
    2. Inputs
    - The hourly wage
    - Total regular hours
    - Total overtime hours
    3. Outputs
    - An employee’s total weekly pay
    4. Design
    - The hourly wage
    - Total regular hours
    - Total overtime hours
    - The formulas are:
    + An employee's total weekly pay = ( the hourly wage * regular hour ) + over time pay
  ....
"""
# Request the inputs
hourlywage=float(input("Nhap luong theo gio cua ban: "))
regularhour=int(input("Nhap thoi gian lam viec trong ngay: "))
overtimehour=int(input("Nhap thoi gian tang ca: "))
overtimepay=overtimehour*1.5
# Compute an employee's total weekly pay
total=(hourlywage*regularhour)+overtimepay
# Display the number of minute of a year
print("Tong luong ma ban nhan duoc trong 1 tuan la: ",total)
