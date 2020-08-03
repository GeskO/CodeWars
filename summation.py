"""Сумирует все числа начиная с 1"""
"""Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer 
greater than 0.

For example:
summation(2) -> 3
1 + 2
summation(8) -> 36
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8"""


def summation(num):
    i = 1
    sum = 0
    while i <= num:
        sum += i
        i += 1
    return (sum)


def summation_v2(num):
    return sum(range(1,num + 1))


summation(1)
summation(8)
summation(22)
summation(100)
summation(213)
