num = int(input("Digite um número inteiro:\n-> "))
fatorial = 1
for i in range(num):
    fatorial = fatorial * (i + 1)
print(f'{num}! = {fatorial}')