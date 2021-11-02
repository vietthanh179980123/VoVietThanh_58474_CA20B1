"""
Author: Võ Viết Thanh
Date: 15/09/2021
Program: An Investment Report
Solution:
    1. Request
    Write a program that computes an investment report.
    2. Analysis
    The inputs to this program are the following:
    • An initial amount to be invested (a floating-point number)
    • A period of years (an integer)
    • An interest rate (a percentage expressed as an integer)
    The program uses a simplified form of compound interest, in which the interest is
    computed once each year and added to the total amount invested. The output of
    the program is a report in tabular form that shows, for each year in the term of the
    investment, the year number, the initial balance in the account for that year, the interest earned for that year, and the ending balance for that year. The columns of the
    table are suitably labeled with a header in the first row. Following the output of the
    table, the program prints the total amount of the investment balance and the total
    amount of interest earned for the period
    3. Design
    The four principal parts of the program perform the following tasks:
    1. Receive the user’s inputs and initialize data.
    2. Display the table’s header.
    3. Compute the results for each year, and display them as a row in the table.
    4. Display the totals.
    The third part of the program, which computes and displays the results, is a loop. The
    following is a slightly simplified version of the pseudocode for the program, without
    the details related to formatting the outputs:
    Input the starting balance, number of years, and interest rate
    Set the total interest to 0.0
    Print the table's heading
    For each year
     compute the interest
     compute the ending balance
     print the year, starting balance, interest, and ending balance
     update the starting balance
     update the total interest
    print the ending balance and the total interest
    Note that starting balance refers to the original input balance and also to the balance
    that begins each year of the term. Ignoring the details of the output at this point allows
    us to focus on getting the computations correct. We can translate this pseudocode to
    a Python program to check our computations. A rough draft of a program is called a
    prototype. Once we are confident that the prototype is producing the correct numbers,
    we can return to the design and work out the details of formatting the outputs.
    The format of the outputs is guided by the requirement that they be aligned nicely in
    columns. We use a format string to right-justify all of the numbers on each row of output. We also use a format string for the string labels in the table’s header. After some
    trial and error, we come up with field widths of 4, 18, 10, and 16 for the year, starting balance, interest, and ending balance, respectively. We can also use these widths
    in the format string for the header.
    4. Implementation (Coding)
    The code for this program shows each of the major parts described in the design, set off by end-of-line comments. Note the use of the many variables to track the
    various amounts of money used by the program. Wisely, we have chosen names for these variables that clearly describe their purpose. The format strings in the print
    statements are rather complex, but we have made an effort to format them so the information they contain is still fairly readable.
    5. Testing
    When testing a program that contains a loop, we should focus first on the input
    that determines the number of iterations. In our program, this value is the number
    of years. We enter a value that yields the smallest possible number of iterations,
    then increase this number by 1, then use a slightly larger number, such as 5, and
    finally we use a number close to the maximum expected, such as 50 (in our problem
    domain, probably the largest realistic period of an investment). The values of the
    other inputs, such as the investment amount and the rate in our program, should
    be reasonably small and stay fixed for this phase of the testing. If the program produces correct outputs for all of these inputs, we can be confident that the loop is
    working correctly.
    In the next phase of testing, we examine the effects of the other inputs on the
    results, including their format. We know that the other two inputs to our programs,
    the investment and the rate, already produce correct results for small values. A reasonable strategy might be to test a large investment amount with the smallest and
    largest number of years and a small rate, and then with the largest number of years
    and the largest reasonable rate. Table 3-1 organizes these sets of test data for the
    program.
    ....
"""
# Accept the inputs
startBalance = float(input("Enter the investment amount: "))
years = int(input("Enter the number of years: "))
rate = int(input("Enter the rate as a %: "))
# Convert the rate to a decimal number
rate = rate / 100
# Initialize the accumulator for the interest
totalInterest = 0.0
# Display the header for the table
print("%4s%18s%10s%16s" % \
("Year", "Starting balance",
"Interest", "Ending balance"))
# Compute and display the results for each year
for year in range(1, years + 1):
interest = startBalance * rate
endBalance = startBalance + interest
print("%4d%18.2f%10.2f%16.2f" % \
(year, startBalance, interest, endBalance))
startBalance = endBalance
totalInterest += interest
# Display the totals for the period
print("Ending balance: $%0.2f" % endBalance)
print("Total interest earned: $%0.2f" % totalInterest)
