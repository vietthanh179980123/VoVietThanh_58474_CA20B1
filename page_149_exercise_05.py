"""
Author: Vo Viet Thanh
Date: 8/10/2021
Program: What is the purpose of a main function?
Solution:
    This function usually expects no arguments and returns no value. Its purpose might be to take inputs,
    process them by calling other functions, and print the results. The definition of the main
    function and the other function definitions need appear in no particular order in the script,
    as long as main is called at the very end of the script. The next example shows a complete
    script that is organized in the manner just described. The main function prompts the user
    for a number, calls the square function to compute its square, and prints the result. You can
    define the main and the square functions in any order. When Python loads this module,
    the code for both function definitions is loaded and compiled, but not executed. Note that
    main is then called within an if statement as the last step in the script. This has the effect of
    transferring control to the first instruction in the main function’s definition
    ....
"""
