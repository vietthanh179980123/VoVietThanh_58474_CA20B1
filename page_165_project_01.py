"""
Author: Vo Viet Thanh
Date: 8/10/2021
Program: A group of statisticians at a local college has asked you to create a set of functions
that compute the median and mode of a set of numbers, as defined in Section
5.4. Define these functions in a module named stats.py. Also include a function
named mean, which computes the average of a set of numbers. Each function
should expect a list of numbers as an argument and return a single number. Each
function should return 0 if the list is empty. Include a main function that tests the
three statistical functions with a given list.
Solution:
    ....
"""
def median(numbers):
    numbers.sort()
    midIndex = len(numbers) // 2
    if len(numbers) % 2 == 1:
        return numbers[midIndex]
    else:
        return (numbers[midIndex] + numbers[midIndex - 1]) / 2
def mean(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)
def mode(numbers):
    result = numbers[0]
    count = 0
    for num in numbers:
        if numbers.count(num) >= count:
            count = numbers.count(num)
            result = num
    return result
def main():
    userList = [3, 1, 7, 1, 4, 10]
    print("Danh sach:", userList)
    print("Che do:", mode(userList))
    print("Trung bình:", median(userList))
    print("Mean:", mean(userList))
main()
