"""
Author: Vo Viet Thanh
Date: 21/10/2021
Program: Explain how an algorithm solves a general class of problems and how a function
definition can support this property of an algorithm.
Solution:
    - How an algorithm solves a general class of problems
    An algorithm is a general method for solving a class of problems. The individual problems
    that make up a class of problems are known as problem instances. The problem instances
    for our summation algorithm are the pairs of numbers that specify the lower and upper
    bounds of the range of numbers to be summed. The problem instances of a given algorithm
    can vary from program to program, or even within different parts of the same program.
    When you design an algorithm, it should be general enough to provide a solution to many
    problem instances, not just one or a few of them. In other words, a function should provide
    a general method with systematic variations.
    - How a function definition can support this property of an algorithm
    The summation function contains both the code for the summation algorithm and the
    means of supplying problem instances to this algorithm. The problem instances are the data
    sent as arguments to the function. The parameters or argument names in the function’s
    header behave like variables waiting to be assigned data whenever the function is called
    ....
"""