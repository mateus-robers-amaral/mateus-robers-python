matriz = []
for i in range(0,2):
    matriz.append([])
    for j in range(0,3):
        matriz[i].append(int(input(f'Digite o valor [{i}][{j}]\n-> ')))

soma = 0
for i in range(0,2):
    for j in range(0,3):
        soma += matriz[i][j]
print(soma)