"""
Author: Võ Viết Thanh
Date: 18/09/2021
Program: Write a program that receives a series of numbers from the user and allows the
user to press the enter key to indicate that he or she is finished providing inputs.
After the user presses the enter key, the program should print the sum of the
numbers and their average.
Solution:
  ....
"""
x=int(input("Nhap so phan tu trong list cua ban: "))
list=[]
tong=0
for y in range(1, x+1):
    list.append(int(input()))
for i in list:
    tong=tong+i
print("Tong cua list la: ", tong)
print("Trung binh cong cua list la: ", tong/x)
