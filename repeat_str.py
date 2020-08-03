"""віводим строку столько раз, сколько задано в функции"""
"""Write a function called repeatString which repeats the given string src exactly count times.

repeatStr(6, "I") // "IIIIII"
repeatStr(5, "Hello") // "HelloHelloHelloHelloHello" """


def repeat_str(repeat, string):
    return string * repeat


repeat_str(4, 'a')
repeat_str(3, 'hello ')
repeat_str(2, 'abc')