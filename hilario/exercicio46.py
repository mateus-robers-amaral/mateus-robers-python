import random

lista = []
while len(lista) < 10:
    num = random.randint(1, 50)
    if num not in lista:
        lista.append(num)
print(lista)
