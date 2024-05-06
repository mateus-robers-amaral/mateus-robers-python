# l = [0] * 5 
# print(l)

# a = list()
# print(a)

# lista = [1, 2, 3, 4, 5]
# x = 0
# while 0 < len(lista):
#     print(lista[x], end=" ")
#     x += 1

# lista = [9, 8, 7, 6, 5]
# for i in range(5):
#     i+=1
#     print(lista[-i], end=" ")

# lista = [1, 2, 3, 2, 1]
# for i in lista:
#     print(i, end=" ")

# lista = [0] * 10
# print(lista)
# for i in range(10):
#     lista[i] = int(input(f"{i+1}° valor -> "))
# print(lista)

# lista = []
# print(lista)
# for i in range(10):
#     valor = int(input(f"{i+1}° valor -> "))
#     lista.append(valor)
# print(lista)

from random import randint
lista = []
for i in range(5):
    lista.append(randint(0, 50))
print(lista)