"""
Author: Vo Viet Thanh
Date: 21/10/2021
Program: What is the lifetime of a variable? Give an example.
Solution:
    - A computer program has two natures. On the one hand, a program is a piece of text containing names that a human being can read for a meaning. Viewed from this perspective,
    variables in a program have a scope that determines their visibility. On the other hand, a
    program describes a process that exists for a period of time on a real computer. Viewed
    from this other perspective, a program’s variables have another important property called a
    lifetime.
    - An example:
    The concept of lifetime explains the existence of two variables called x in our last
    example session. The module variable x comes into existence before the temporary variable x and survives the call of function f. During the call of f, storage exists for both
    variables, so their values remain distinct. A similar mechanism for managing the storage associated with the parameters of recursive function calls was discussed in the previous section.
    ....
"""