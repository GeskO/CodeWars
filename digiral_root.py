"""цифровой корень числа"""
"""Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way 
until a single-digit number is produced. This is only applicable to the natural numbers.

Examples
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2"""


def digital_root(n):
    first = n
    res = []
    while n > 10:
        arr = []
        while n > 0:
            arr.insert(0, n % 10)
            n = n // 10
        sum = 0
        for i in arr:
            sum += i
        n = sum
        res.append(arr)
    print(f"{first}", end=" ")
    for row in res:
        print("-->", end=" ")
        print(' + '.join([str(elem) for elem in row]), end=" ")
    print(f"= {sum}")
    return sum


digital_root(16)
digital_root(942)
digital_root(132189)
digital_root(493193)
