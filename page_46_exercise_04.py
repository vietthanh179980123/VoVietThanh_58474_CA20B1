"""
Author: Võ Viết Thanh
Date: 03/09/2021
Program: What happens when the print function prints a string literal with embedded
newline characters?
Solution:
    - Example: We write this string in the Python shell: 
    >>> print("""This very long sentence extends all the way to the next line.""")
    - It's will display this sentence: 
    "SyntaxError: invalid syntax
    >>> print("""This very long sentence extends... all the way to the next\n line."""")
    This very long sentence extends
    all the way to the next

    ....
"""
