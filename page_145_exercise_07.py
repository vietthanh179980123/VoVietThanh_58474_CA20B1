"""
Author: Vo Viet Thanh
Date: 8/10/2021
Program: Describe the costs and benefits of aliasing, and explain how it can be avoided.
Solution:
    - The costs:
    + As you might imagine,aliasing is not always a good thing when side effects are possible
    + Although this behavior can be useful, it is sometimes unexpected or undesirable
    - The benefits:
    + If the data are immutable strings, aliasing can save on memory
    + Assignment creates an alias to the same object rather than a reference to a copy of the object
    ....
"""
