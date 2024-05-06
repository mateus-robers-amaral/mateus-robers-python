from random import randint
lista = []
for i in range(20):
    lista.append(randint(1, 50))
print(lista)

multiplos = []
base = int(input("Digite um número:\n--> "))
for num in lista:
    if num % base == 0:
        multiplos.append(num)
print(f"Os números aleatórios múltiplos de {base} são: {multiplos}")