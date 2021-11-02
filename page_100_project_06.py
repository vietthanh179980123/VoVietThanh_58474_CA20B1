"""
Author: Võ Viết Thanh
Date: 18/09/2021
Program: The German mathematician Gottfried Leibniz developed the following method
to approximate the value of π: π/4 5 1 ] 1/3 1 1/5 ] 1/7 1 . . .
Solution:
  ....
"""
repeat = int(input("Nhap so lan lap lai: "))
list01 = []
list02 = []
y = 1
for x in range(1, repeat + 1):
    number = (1.0 / y)
    list01.append(number)
    y += 2.0
for i in range(1, repeat, 2):
    neg = list01[i] * -1.0
    list02.append(neg)
comb = (sum(list01)) + (sum(list02)) + (sum(list02))
pi = comb * 4.0
print("Gia tri sap xi cua pi la: ", pi)
