from random import randint
lista = []
for i in range(10):
    lista.append(randint(1, 50))
print(lista)
quest = int(input("Digite um valor x:\n--> "))
mult = []
for num in lista:
    mult.append(quest * num)
print(mult)