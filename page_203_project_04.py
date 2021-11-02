"""
Author: Vo Viet Thanh
Date: 23/10/2021
Program: Restructure Newton’s method (Case Study 3.6) by decomposing it into three
cooperating functions. The newton function can use either the recursive strategy
of Project 1 or the iterative strategy of Case Study 3.6. The task of testing for the
limit is assigned to a function named limitReached, whereas the task of computing a new approximation is assigned to a function named improveEstimate. Each
function expects the relevant arguments and returns an appropriate value.
Solution:
    ....
"""
import math
tolerance = 0.000001

def newton(x, estimate=1):
    if limitreached(x, estimate):
        return estimate
    else:
        return newton(x, improveestimate(x, estimate))
def limitreached(x, estimate):
    difference = abs(x - estimate ** 2)
    return difference <= tolerance
def improveestimate(x, estimate):
    return (estimate + x / estimate) / 2
def main():
    while True:
        x = input("Nhập số dương hoặc enter/return để thoát:")
        if x == "":
            break
        x = float(x)
        print("The program's estimate is: ", newton(x))
        print("Python's estimate is       ", math.sqrt(x))

main()
