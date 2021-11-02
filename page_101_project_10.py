"""
Author: Võ Viết Thanh
Date: 18/09/2021
Program: The credit plan at TidBit Computer Store specifies a 10% down payment and
an annual interest rate of 12%. Monthly payments are 5% of the listed purchase
price, minus the down payment. Write a program that takes the purchase price
as input. The program should display a table, with appropriate headers, of a payment schedule for the lifetime of the loan. Each row of the table should contain
the following items:
• the month number (beginning with 1)
• the current total balance owed
• the interest owed for that month
• the amount of principal owed for that month
• the payment for that month
• the balance remaining after payment
The amount of interest for a month is equal to balance * rate / 12. The amount of
principal for a month is equal to the monthly payment minus the interest owed
Solution:
  ....
"""
price=int(input("Nhap gia tien: "))
month=int(input("Nhap so thang phai tra gop:"))
monthly_pay=5/100
down_pay=10/100
year_pay=12/100
down=price-(down_pay*price)
for count1 in range(1,month+1):
    print("Thang", count1 , "So tien phai tra theo thang", (down*year_pay)*monthly_pay)
print("Month number ", ((down*year_pay)*month)-(down*year_pay))
print("Current ",(down/month)-(down*year_pay))
print("Interest owed ",(down/month))
print("Payment  ",(down*year_pay)*monthly_pay)
print("Balance ",)



