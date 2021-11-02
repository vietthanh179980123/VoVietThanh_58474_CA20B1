"""
Author: Võ Viết Thanh
Date: 16/09/2021
Program: The variables x and y refer to numbers. Write a code segment that prompts the user for
an arithmetic operator and prints the value obtained by applying that operator to x and y
Solution:
  ....
"""
x=int(input("Nhap so thu 1: "))
y=int(input("Nhap so thu 2: "))
nhaptoantu = int(input("Nhap lua chon cua ban: "))
if nhaptoantu==1:
    print("Phep tinh cho x va y la: ",x+y)
elif nhaptoantu==2:
    print("Phep tinh cho x va y la: ",x-y)
elif nhaptoantu==3:
    print("Phep tinh cho x va y la: ",x*y)
elif nhaptoantu==4:
    print("Phep tinh cho x va y la: ",x/y)
elif nhaptoantu==5:
    print("Phep tinh cho x va y la: ",x**y)
else:
    print("Khong co phep tinh!")



