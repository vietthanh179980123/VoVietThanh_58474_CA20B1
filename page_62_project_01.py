"""
Author: Võ Viết Thanh
Date: 04/09/2021
Program: The tax calculator program of the case study outputs a floating-point number
that might show more than two digits of precision. Use the round function to
modify the program to display at most two digits of precision in the output
number.
Solution:
    1. Analys
    - The program is requested that computes a person's income tax, and we use the round function to modify the program to display at most 2 digits of precision in the output
    2. Inputs
    - grossIncome
    - numDependents
    3. Outputs
    - taxableIncome
    - incomeTax rounded to 2 figures
    4. Design
    - Initialize the constants
    + TAX_RATE
    + STANDARD_DEDUCTION
    + DEPENDENT_DEDUCTION
    - Compute the income tax
    + taxableIncome = grossIncome - STANDARD_DEDUCTION - \
    + DEPENDENT_DEDUCTION * numDependents
    + incomeTax = taxableIncome * TAX_RATE

  ....
"""
# Initialize the constants
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0
# Request the inputs
grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))
# Compute the income tax
taxableIncome = grossIncome - STANDARD_DEDUCTION - \
 DEPENDENT_DEDUCTION * numDependents
incomeTax = taxableIncome * TAX_RATE
# Display the income tax
print("The income tax is $" + str(incomeTax))
round(incomeTax,2)
