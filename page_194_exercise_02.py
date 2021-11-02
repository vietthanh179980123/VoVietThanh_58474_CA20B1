"""
Author: Vo Viet Thanh
Date: 21/10/2021
Program: What is the scope of a variable? Give an example.
Solution:
    - In ordinary writing, the meaning of a word often depends on its surrounding context. For
    example, in the sports section of the newspaper, the word “bat” means a stick for hitting
    baseballs, whereas in a story about vampires it means a flying mammal. In a program, the
    context that gives a name a meaning is called its scope
    - An example:
    x = 5
    def f():
        x = 10 # Attempt to reset x
    f() # Does the top-level x change?
    print(x) # No, this displays 5
    When the function f is called, it does not assign 10 to the module variable x; instead, it assigns
    10 to a temporary variable x. In fact, once the temporary variable is introduced, the module
    variable is no longer visible within function f. In any case, the module variable’s value remains
    unchanged by the call. There is a way to allow a function to modify a module variable, but in
    Chapter 9 we explore a better way to manage common pools of data that require changes.
    ....
"""