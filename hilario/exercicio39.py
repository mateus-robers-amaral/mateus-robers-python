from random import randint
lista = []
for i in range(10):
    lista.append(randint(1, 50))
print(lista)

pares = []
impares = []

for num in lista:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print(f"O número de números pares é {len(pares)}\nO número de números ímpares é {len(impares)}")