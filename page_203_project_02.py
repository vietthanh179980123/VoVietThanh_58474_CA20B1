"""
Author: Vo Viet Thanh
Date: 23/10/2021
Program: Convert Newton’s method for approximating square roots in Project 1 to a recursive function named newton. (Hint: The estimate of the square root should be
passed as a second argument to the function.)
Solution:
    ....
"""
import math
tolerance = 0.000001

def newton(x, estimate):
    difference = abs(x - estimate ** 2)
    if difference <= tolerance:
        return estimate
    else:
        estimate = (estimate + x / estimate) / 2
        return newton(x, estimate)
def main():
    while True:
        x = input("Nhập số dương hoặc enter/return để thoát:")
        if x == "":
            break
        x = float(x)
        print("The program's estimate is: ", newton(x, 1))
        print("Python's estimate is       ", math.sqrt(x))

main()

