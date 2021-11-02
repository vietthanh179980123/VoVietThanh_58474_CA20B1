"""
Author: Vo Viet Thanh
Date: 24/10/2021
Program: Define and test a function myRange. This function should behave like Python’s
standard range function, with the required and optional arguments, but it should
return a list. Do not use the range function in your implementation! (Hints:
Study Python’s help on range to determine the names, positions, and what to do
with your function’s parameters. Use a default value of None for the two optional
parameters. If these parameters both equal None, then the function has been
called with just the stop value. If just the third parameter equals None, then the
function has been called with a start value as well. Thus, the first part of the function’s code establishes what the values of the parameters are or should be. The
rest of the code uses those values to build a list by counting up or down.)
Solution:
    ....
"""
def myrange(start, stop=None, step=None):
    lyst=[]
    if stop == None and step==None:
        stop = start
        start = 0
        step = 1
    if start < stop:
        if step == None:
            step=1
        elif step <=0:
            return lyst
        while start < stop:
            lyst.append(start)
            start+=step
    else:
        if step == None or step>-1:
            return lyst
        while start>stop:
            lyst.append(start)
            start+=step
    return lyst
def main():
    print(myrange(10))
    print(myrange(1,10))
    print(myrange(1,10,2))
    print(myrange(10,1,-1))

main()
