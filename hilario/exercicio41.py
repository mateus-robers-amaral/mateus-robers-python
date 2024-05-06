from random import randint
lista = []
cinco = []
for num in range(20):
    lista.append(randint(1, 50))

for i in lista:
    if i % 5 == 0:
        cinco.append(i) 
print(lista)
print(f"Os múltiplos de 5 são: {cinco}")
