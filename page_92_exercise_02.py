"""
Author: Võ Viết Thanh
Date: 17/09/2021
Program: The factorial of an integer N is the product of the integers between 1 and N, inclusive. Write a while loop that computes the factorial of a given integer N
Solution:
  ....
"""
N=int(input("Nhap so vao day: "))
giaithua=1
i=1
while i<=N:
    giaithua = giaithua * i
    i+=1
print("Giai thua cua so nay la: ", giaithua)


