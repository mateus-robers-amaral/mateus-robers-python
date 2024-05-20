import random
matriz = []
for i in range(0,10):
    matriz.append([])
    for j in range(0,10):
        matriz[i].append(random.randint(1,50))
print(matriz)

for i in range(0,10):
    for j in range(0,10):
        media = matriz[i][j] / len(matriz)

print(media)