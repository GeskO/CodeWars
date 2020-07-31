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
