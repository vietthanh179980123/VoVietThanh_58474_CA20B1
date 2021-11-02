"""
Author: Vo Viet Thanh
Date: 8/10/2021
Program: Assume that the variable data refers to the list [5, 3, 7]. Write the expressions
that perform the following tasks:
    a. Replace the value at position 0 in data with that value’s negation.
    b. Add the value 10 to the end of data.
    c. Insert the value 22 at position 2 in data.
    d. Remove the value at position 1 in data
    e. Add the values in the list newData to the end of data.
    f. Locate the index of the value 7 in data, safely.
    g. Sort the values in data.
Solution:
    a.list = [5,3,7]
    list[0]=-5
    list
    b.list = [5,3,7]
    list[2]=10
    list
    c.list =[5,3,7]
    list[1]=22
    list
    d.list = [5,3,7]
    list.pop(0)
    list
    e.new_data=[1,2,3]
    new_data.append(6)
    new_data
    f. list = [5,3,7]
    target = 7
    if target in list:
        print(list.index(target))
    else:
        print(-l)
    f. list = [5,3,7]
    list.sort()
    list
    ....
"""
