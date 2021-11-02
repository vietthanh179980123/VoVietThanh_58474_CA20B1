"""
Author: Vo Viet Thanh
Date: 8/10/2021
Program: What is a mutator method? Explain why mutator methods usually return the
value None.
Solution:
    - Mutable objects (such as lists) have some methods devoted
    entirely to modifying the internal state of the object.Such methods are called mutators
    -  Because a change of state is all that is desired, a mutator method usually returns no value of interest to the caller(but note that
    pop is an exception to this rule) Python nevertheless automatically returns the special value None
    even when a method does not explicitly return a value. We mention this now only as a warning
    against the following type of error
    ....
"""
