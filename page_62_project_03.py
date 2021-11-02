"""
Author: Võ Viết Thanh
Date: 04/09/2021
Program: Five Star Retro Video rents VHS tapes and DVDs to the same connoisseurs who
like to buy LP record albums. The store rents new videos for $3.00 a night, and
oldies for $2.00 a night. Write a program that the clerks at Five Star Retro Video
can use to calculate the total charge for a customer’s video rentals. The program
should prompt the user for the number of each type of video and output the total
cost.
Solution:
    1. Analys
    - Calcaculate the total charge for a customer’s video rentals
    2. Inputs
    - newOnes
    - oldOnes
    3. Outputs
    - the total cost
    4. Design
    - Initialize the constants
    + New_video = 3.00
    + Oldies_video = 2.00
    - Input the newOnes and oldiesOnes to calculate the total cost. The formula is total = newOnes * New_video + oldOnes * Oldies_video
  ....
"""
# Initialize the constants
New_video = 3.00
Oldies_video = 2.00
# Request the inputs
newOnes = int(input("Nhap so luong dia moi duoc thue: "))
oldOnes = int(input("Nhap so luong dia cu duoc thue: "))
# Compute the total cost
total = (newOnes * New_video) + (oldOnes * Oldies_video)
# Display the total cost
print("Tong so tien phai tra la: ", total)
