from random import randint
lista = []
for i in range(20):
    lista.append(randint(1, 50))
print(lista)

pares = []
for num in lista:
    if num % 2 == 0:
        pares.append(num)

media = 0
for i in range(len(pares)):
    media += pares[i]

print(f"A média dos números pares é {media/len(pares)}.") 