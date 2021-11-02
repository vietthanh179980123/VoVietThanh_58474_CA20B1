"""
Author: Võ Viết Thanh
Date: 18/09/2021
Program: Teachers in most school districts are paid on a schedule that provides a salary
based on their number of years of teaching experience. For example, a beginning
teacher in the Lexington School District might be paid $30,000 the first year. For
each year of experience after this first year, up to 10 years, the teacher receives a
2% increase over the preceding value. Write a program that displays a salary schedule, in tabular format, for teachers in a school district. The inputs are the starting
salary, the percentage increase, and the number of years in the schedule. Each row
in the schedule should contain the year number and the salary for that year.
Solution:
  ....
"""
st_salary=float(input("Luong ban dau cua giang vien nay la: "))
percent=int(input("Nhap he so luong: "))
years=int(input("Nhap so nam ma giang vien nay da lam: "))
percent=percent/100
for count in range(1, years+1):
    print("Nam", count, "Luong theo nam", st_salary*((1+percent)**(count-1)))




