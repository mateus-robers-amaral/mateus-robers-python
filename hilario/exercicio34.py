for num in range(1000, 10000):
    first = num // 100
    last = num % 100
    third = first + last
    if third ** 2 == num:
        print(num)