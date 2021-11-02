"""
Author: Vo Viet Thanh
Date: 21/10/2021
Program: Write the code for a reducing that creates a single string from a list of strings named
words
Solution:
    ....
"""
words = ['alfa', 'bravo', 'charlie', 'delta', 'gamma', 'lambda']
from functools import reduce
print(reduce(lambda x,y:x+y,map(lambda x:x[0],words)))