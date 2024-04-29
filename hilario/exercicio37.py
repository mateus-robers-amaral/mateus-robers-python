primos = []
for num in range(0, 1000):
    contador = 0
    for i in range(1, num + 1):
        if num % i == 0:
            contador += 1
    if contador == 2:
        primos.append(num)
    num += 1

print(primos)