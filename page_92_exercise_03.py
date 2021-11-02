"""
Author: Võ Viết Thanh
Date: 17/09/2021
Program: The log 2 of a given number N is given by M in the equation N 5 2M. Using integer
arithmetic, the value of M is approximately equal to the number of times N can be
evenly divided by 2 until it becomes 0. Write a loop that computes this approximation of the log 2 of a given number N. You can check your code by importing the
math.log function and evaluating the expression round(math.log(N, 2)) (note
that the math.log function returns a floating-point value)
Solution:
  ....
"""
import math
n=int(input("Nhap n: "))
for m in range(1):
    print("Logarit cua",n,"la: ", round(math.log(n, 2)))



