"""
Author: Võ Viết Thanh
Date: 15/09/2021
Program: Write a loop that outputs the numbers in a list named salaries. The outputs should be
formatted in a column that is right-justified, with a field width of 12 and a precision of 2.
Solution:

  ....
"""

salaries = [2.456,4.56789,82.3485,90.32019]
for i in salaries:
    print("%12s.2f" % i)

