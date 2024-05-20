import random
matriz = []
for i in range(0,10):
    matriz.append([])
    for j in range(0,10):
        matriz[i].append(random.randint(5,38))
print(matriz)

total = 0
for i in range(0,10):
    soma = 0
    for j in range(0,10):
        soma += matriz[i][j]
    total += soma
print(total)