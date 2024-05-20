import random
matriz = []
for i in range(0,10):
    matriz.append([])
    for j in range(0,10):
        matriz[i].append(random.randint(1,50))
    print(matriz[i])
print()

menor = 51
for i in range(0, 10):
    for j in range(0, 10):
        if matriz[j][i] < menor:
            menor = matriz[j][i]
    print(menor)
    menor = 51