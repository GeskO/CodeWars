"""Вернуть к какому веку относится данный год"""
"""Introduction
The first century spans from the year 1 up to and including the year 100, 
The second - from the year 101 up to and including the year 200, etc.

Task :
Given a year, return the century it is in.

Input , Output Examples ::
centuryFromYear(1705)  returns (18)
centuryFromYear(1900)  returns (19)
centuryFromYear(1601)  returns (17)
centuryFromYear(2000)  returns (20)
Hope you enjoy it .. Awaiting for Best Practice Codes

Enjoy Learning !!!"""
import math

def century(year):
    res = year // 100
    if year % 100 != 0:
        res += 1
    return res


def century_v2(year):
    return (year + 99) // 100


def century_v3(year):
    return math.ceil(year / 100)


century(1705)  # 18, 'Testing for year 1705')
century(1900)  # 19, 'Testing for year 1900')
century(1601)  # 17, 'Testing for year 1601')
century(2000)  # 20, 'Testing for year 2000')
century(356)  # 4, 'Testing for year 356')
century(89)  # 1, 'Testing for year 89')
