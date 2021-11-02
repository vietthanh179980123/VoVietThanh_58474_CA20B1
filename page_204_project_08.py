"""
Author: Vo Viet Thanh
Date: 23/10/2021
Program: Lee has discovered what he thinks is a clever recursive strategy for printing the
elements in a sequence (string, tuple, or list). He reasons that he can get at the
first element in a sequence using the 0 index, and he can obtain a sequence of
the rest of the elements by slicing from index 1. This strategy is realized in a
function that expects just the sequence as an argument. If the sequence is not
empty, the first element in the sequence is printed and then a recursive call is
executed. On each recursive call, the sequence argument is sliced using the
range 1:. Here is Lee’s function definition:
def printAll(seq):
if seq:
print(seq[0])
printAll(seq[1:])
Write a script that tests this function and add code to trace the argument on each
call. Does this function work as expected? If so, explain how it actually works,
and describe any hidden costs in running it.
Solution:
    ....
"""
def printall(seq):
    if seq:
        print(seq, "->", seq[0])
        printall(seq[1:])

printall(list(range(10)))