"""
Author: Võ Viết Thanh
Date: 17/09/2021
Program: Modify the guessing-game program of Section 3.5 so that the user thinks of a
number that the computer must guess. The computer must make no more than
the minimum number of guesses, and it must prevent the user from cheating by
entering misleading hints. (Hint: Use the math.log function to compute the minimum number of guesses needed after the lower and upper bounds are entered.
Solution:
  ....
"""
import random
import math
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
rand_num = random.randint(0, 100)
guesses = round(math.log(100 - 0 + 1, 2))
print("Ban co", guesses, "lan de doan so!\n")
myNumber = random.randint(smaller, larger)
count = 0
while True:
    count += 1
    if count > guesses:
        print("Vuot toi da so lan doan.")
        print("So lan doan la ",rand_num)
        break
    userNumber = int(input("Enter your guess: "))
    if userNumber < myNumber:
        print("Too small!")
    elif userNumber > myNumber:
        print("Too large!")
    else:
        print("Congratulations! You've got it in", count,"tries!")
        break
