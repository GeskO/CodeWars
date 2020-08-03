"""Перевернуть строку"""
"""Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'"""


def solution(string):
    return string[::-1]


solution('world')  # 'dlrow')
solution('hello')  # 'olleh')
solution('')  # '')
solution('h')  # 'h')
