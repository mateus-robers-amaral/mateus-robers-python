from random import randint
escolha = int(input("[1] Ordem normal\n[2] Ordem inversa\n--> "))
lista = []
for i in range(20):
    lista.append(randint(1, 50))
if escolha == 1:
    lista.sort()
    print(lista)
    
elif escolha == 2:
    lista.sort(reverse=True)
    print(lista)