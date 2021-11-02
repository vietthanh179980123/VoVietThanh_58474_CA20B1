"""
Author: Võ Viết Thanh
Date: 17/09/2021
Program: A local biologist needs a program to predict population growth. The inputs
would be the initial number of organisms, the rate of growth (a real number
greater than 0), the number of hours it takes to achieve this rate, and a number
of hours during which the population grows. For example, one might start with a
population of 500 organisms, a growth rate of 2, and a growth period to achieve
this rate of 6 hours. Assuming that none of the organisms die, this would imply
that this population would double in size every 6 hours. Thus, after allowing
6 hours for growth, we would have 1000 organisms, and after 12 hours, we would
have 2000 organisms. Write a program that takes these inputs and displays a prediction of the total population.
Solution:
  ....
"""
number=int(input("Nhap so luong ban dau: "))
rate=int(input("Nhap toc do tang truong: "))
hours_take=int(input("Nhap thoi gian can thiet de dat toc do tang truong: "))
hours_grow=int(input("Nhap tong thoi gian trong qua trinh tang truong:  "))
hours=0
total=int()
while hours_take<hours_grow:
    total=number*rate
    total=total*2
    hours=hour+hours_take
    if hour==hours_grow:
        break
print("So luong sinh vat tang trong",hours_grow,"gio la: ",total)
