"""
Author: Vo Viet Thanh
Date: 21/10/2021
Program: The factorial of a positive integer n, fact(n), is defined recursively as follows:
    fact( ) n 1 5 , when n 1 5
    fact( ) n n 5 2 * fact n ( ) 1 , otherwise
    Define a recursive function fact that returns the factorial of a given positive
    integer.
Solution:
    ....
"""
def fact(n):
    if n==1:
        return 1
    else:
        return n * fact(n-1)
