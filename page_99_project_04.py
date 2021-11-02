"""
Author: Võ Viết Thanh
Date: 17/09/2021
Program: A standard science experiment is to drop a ball and see how high it bounces.
Once the “bounciness” of the ball has been determined, the ratio gives a bounciness index. For example, if a ball dropped from a height of 10 feet bounces 6 feet
high, the index is 0.6, and the total distance traveled by the ball is 16 feet after
one bounce. If the ball were to continue bouncing, the distance after two bounces would be 10 ft 6 ft 6 ft 3.6 ft 25.6 ft 111 5 . Note that the distance traveled for
each successive bounce is the distance to the floor plus 0.6 of that distance as the
ball comes back up. Write a program that lets the user enter the initial height
from which the ball is dropped and the number of times the ball is allowed to
continue bouncing. Output should be the total distance traveled by the ball.
Solution:
  ....
"""
height=int(input("Nhap chieu cao ban dau: "))
number=int(input("Nhap so lan bong nay: "))
bouciness=int(input("Nhap do nay cua bong: "))
index=bouciness/height
print("He so nay cua bong la: ",index)
total=float()
if number==1:
    total=height+bouciness
    print("Quang duong bong di duoc sau lan nay thu 1 la: ",total)
else:
    total=height+(bouciness*number)+(bouciness*number*index)
    print("Quang duong bong di duoc sau lan nay thu", number ,"la: ",total)

