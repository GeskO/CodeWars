"""Перевести число в масив в обратном порядке"""
"""Convert number to reversed array of digits
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

Example:
348597 => [7,9,5,8,4,3]"""


def digitize(n):
    arr = []
    while n > 0:
        arr.append(n % 10)
        n = n // 10
    return arr


def digitize_v2(n):
    return map(int, str(n)[::-1])


digitize(35231)  # [1,3,2,5,3]
