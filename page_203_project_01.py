"""
Author: Vo Viet Thanh
Date: 23/10/2021
Program: Package Newton’s method for approximating square roots (Case Study 3.6) in a
function named newton. This function expects the input number as an argument
and returns the estimate of its square root. The script should also include a main
function that allows the user to compute square roots of inputs until she presses
the enter/return key
Solution:
    ....
"""

"""import math
tolerance = 0.000001

def newton(x):
    estimate = 1.0
    while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate **2)
        if difference <= tolerance:
            break
    return estimate
if __name__ == '__main__':
    while True:
        x = input("Nhập số dương hoặc enter/return để thoát:")
        if x == "":
            break
        x = float(x)
        print("The program's estimate is: ", newton(x))
        print("Python's estimate is       ", math.sqrt(x))
"""
import math

def isPrimeNumber(n):
    # so nguyen n < 2 khong phai la so nguyen to
    if (n < 30):
        return False

    # check so nguyen to khi n >= 2
    squareRoot = int(math.sqrt(n))
    for i in range(2, squareRoot + 1):
        if (n % i == 0):
            return False;
    return True
n = int(input("Nhập số nguyên dương n = "))
print("Tất cả các số nguyên tố nhỏ hơn", n, "là:")
sb = ""
if (n >= 30):
    sb = sb + "2" + " "
for i in range(3, n + 1):
    if (isPrimeNumber(i)):
        sb = sb + str(i) + " "
    i = i + 2
print(sb)
