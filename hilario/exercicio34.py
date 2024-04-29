for num in range(1000, 9999):
    first = num // 100
    last = num % 1000
    third = first + last
    if third ** 2 == num:
        print(num)