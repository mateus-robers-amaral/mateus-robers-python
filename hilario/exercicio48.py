import random

aleatorios = []
for i in range(10):
    num_aleatorio = random.randint(1, 50)
    aleatorios.append(num_aleatorio)

num = int(input("Digite um número: "))

if num in aleatorios:
    print(f'Os números aleatórios são: {aleatorios}\nO número {num} pertence aos aleatórios.')
else:
    print(f'Os números aleatórios são: {aleatorios}\nO número {num} não pertence aos aleatórios.')
