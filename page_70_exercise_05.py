"""
Author: Võ Viết Thanh
Date: 15/09/2021
Program: Assume that the variable teststring refers to a string. Write a loop that prints
each character in this string, followed by its ASCII value
Solution:

  ....
"""
teststr = input("Put your string in here : ")
for i in range(len(teststr)):
    print("The ASCII Value of Character %c = %d" %(teststr[i], ord(teststr[i])))
