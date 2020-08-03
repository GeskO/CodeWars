"""Посчитать сколько "овец на своих местах" в масиве"""
"""Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts
the number of sheep present in the array (true means present).

For example,

[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
The correct answer would be 17.

Hint: Don't forget to check for bad values like null/undefined"""


def count_sheeps(sheep):
    i = 0
    for e in sheep:
        if e:
            i += 1
    return i


def count_sheeps_v2(sheep):
    return sheep.count(True)


array1 = [True, True, True, False,
          True, True, True, True,
          True, False, True, False,
          True, False, False, True,
          True, True, True, True,
          False, False, True, True]

count_sheeps(array1)
