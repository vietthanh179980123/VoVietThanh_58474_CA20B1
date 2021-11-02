"""
Author: Võ Viết Thanh
Date: 15/09/2021
Program: Write a code segment that displays the values of the integers x, y, and z on a single
line, such that each value is right-justified with a field width of 6.
Solution:
  ....
"""
x=int(input("Nhap so x: "))
y=int(input("Nhap so y: "))
z=int(input("Nhap so z: "))
print( "%-6s" % x,"%-6s" % y,"%-6s" % z)

