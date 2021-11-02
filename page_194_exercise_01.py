"""
Author: Vo Viet Thanh
Date: 21/10/2021
Program: Where are module variables, parameters, and temporary variables introduced and
initialized in a program?
Solution:
    - Module variables:
    + Introduced:
    The names replacements and changePerson are introduced at the
    level of the module
    + Initialized:
    When module variables are introduced in a program, they are immediately given a value.
    - Parameters:
    + Introduced:
    In a function or method header
    + Initialized:
    The parameter does not receive a value until the function is called
    - Temporary variables:
    + Introduced:
    In the body of the function changePerson
    + Initialized:
    Like module variables, temporary variables receive their values as soon as they are introduced.
    ....
"""