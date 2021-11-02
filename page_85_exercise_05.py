"""
Author: Võ Viết Thanh
Date: 16/09/2021
Program: Explain how to check for an invalid input number and prevent it being used in a
program. You may assume that the user enters a number.
Solution:

  ....
"""
# Giả sử đoạn chương trình yêu cầu nhập số dương nếu số âm thì không hợp lệ
numbers = int(input("Nhap so cua ban vao day: "))
if numbers >0:
    print("Day la so hop le!")
else:
    print("Day khong phai la so hop le!")
