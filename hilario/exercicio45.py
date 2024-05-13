import random

numeros = []
for i in range(10):
    num = random.randint(1, 50)
    numeros.append(num)

print(numeros)

numeros_crescente = []
numero = 51
for i in range(10):
    menor = min(numeros)
    numeros_crescente.append(menor)
    numeros.remove(menor)

print(numeros_crescente)

'''Jeito do Hilário'''
from random import randint

lista = []

for i in range(10):
    lista.insert(i, randint(1, 50))

print(f'Vetor gerado: \n{lista}')

for i in range(10):
    for j in range(i + 1, 10):
        if lista[i] > lista[j]:
            list[i], lista[j] = lista[j], lista[i]
print(f'Vetor gerado: \n{lista}')