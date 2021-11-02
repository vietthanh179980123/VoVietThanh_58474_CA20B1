"""
Author: Võ Viết Thanh
Date: 16/09/2021
Program: Assume that the variables x and y refer to strings. Write a code segment that prints
these strings in alphabetical order. You should assume that they are not equal.
Solution:

  ....
"""
x=input("Nhap chuoi x: ")
y=input("Nhap chuoi y: ")
words_x = [word.lower() for word in x.split()]
words_y = [word.lower() for word in y.split()]
words_x.sort()
words_y.sort()
print("Ki tu trong chuoi x la:  ")
for word1 in words_x:
    print(word1)
print("Ki tu trong chuoi y la: ")
for word2 in words_y:
    print(word2)





