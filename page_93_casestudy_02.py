"""
Author: Võ Viết Thanh
Date: 15/09/2021
Program:  Approximating Square Roots
Solution:
    1. Request
    Write a program that computes square roots.
    2. Analysis
    The input to this program is a positive floating-point number or an integer. The output is a floating-point number representing the square root of the input number. For
    purposes of comparison, we also output Python’s estimate of the square root using
    math.sqrt. Here is the proposed user interface:
    Enter a positive number: 3
    The program's estimate: 1.73205081001
    Python's estimate: 1.73205080757
    3. Design
    In the seventeenth century, Sir Isaac Newton discovered an algorithm for approximating the square root of a positive number. Recall that the square root y of a positive
    number x is the number y such that 2 5 y x. Newton discovered that if one’s initial
    estimate of y is z, then a better estimate of y can be obtained by taking the average of z together with x / z. The estimate can be transformed by this rule again and
    again, until a satisfactory estimate is reached.
    A quick session with the Python interpreter shows this method of successive approximations in action. We let x be 25 and our initial estimate, z, be 1. We then use Newton’s method to reset z to a better estimate and examine z to check it for closeness
    to the actual square root, 5. Here is a transcript of our interaction:
    After three transformations, the value of z is exactly equal to 5, the square root of
    25. To include cases of numbers, such as 2 and 10, with irrational square roots, we
    can use an initial guess of 1.0 to produce floating-point results.
    >>> x = 25
    >>> y = 5
    >>> z = 1
    # The actual square root of x
    # Our initial approximation
    >>> z = (z + x / z) / 2
    >>> z
    # Our first improvement
    13.0
    >>> z = (z + x / z) / 2 # Our second improvement
    >>> z
    7.0
    >>> z = (z + x / z) / 2 # Our third improvement – got it!
    We now develop an algorithm to automate the process of successive transformations, because there might be many of them, and we don’t want to write them all.
    Exactly how many of these operations are required depends on how close we want
    our final approximation to be to the actual square root. This closeness value, called
    the tolerance, can be compared to the difference between and the value of x and the
    square of our estimate at any given time. While this difference is greater than the tolerance, the process continues; otherwise, it stops. The tolerance is typically a small
    value, such as 0.000001.
    Our algorithm allows the user to input the number, uses a loop to apply Newton’s
    method to compute the square root, and prints this value. Here is the pseudocode,
    followed by an explanation:
    set x to the user's input value
    set tolerance to 0.000001
    set estimate to 1.0
    while True
     set estimate to (estimate + x / estimate) / 2
     set difference to abs(x - estimate ** 2)
     if difference <= tolerance:
     break
    output the estimate
    Because our initial estimate is 1.0, the loop must compute at least one new estimate.
    Therefore, we use a while True loop. This loop transforms the estimate before
    determining whether it is close enough to the tolerance value to stop the process.
    The process should stop when the difference between the square of our estimate and
    the original number becomes less than or equal to the tolerance value. Note that this
    difference may be positive or negative, so we use the abs function to obtain its absolute value before examining it.
    A more orthodox use of the while loop would compare the difference to the tolerance in the loop header. However, the difference must then be initialized before
    the loop to a large and rather meaningless value. The algorithm presented here
    captures the logic of the method of successive approximations more cleanly and
    simply
    4. Implementation (Coding)
    The code for this program is straightforward.
    5. Testing
    The valid inputs to this program are positive integers and floating-point numbers.
    The display of Python’s own most accurate estimate of the square root provides
    a benchmark for assessing the correctness of our own algorithm. We should at
    least provide a couple of perfect squares, such as 4 and 9, as well as numbers
    whose square roots are inexact, such as 2 and 3. A number between 1 and 0,
    such as .25, should also be included. Because the accuracy of our algorithm
    also depends on the size of the tolerance, we might alter this value during testing
    as well.
    ....
"""
import math
# Receive the input number from the user
x = float(input("Enter a positive number: "))
# Initialize the tolerance and estimate
tolerance = 0.000001
estimate = 1.0
# Perform the successive approximations
while True:
estimate = (estimate + x / estimate) / 2
difference = abs(x - estimate ** 2)
if difference <= tolerance:
break
# Output the result
print("The program's estimate:", estimate)
print("Python's estimate: ", math.sqrt(x))
