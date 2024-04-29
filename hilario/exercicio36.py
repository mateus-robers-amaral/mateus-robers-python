num = int(input("Digite um número:\n-> "))
div = 0
for i in range(1, num + 1):
    if num % i == 0:
        div += 1
''' se o programa conseguir resto = 0 apenas 2 vezes, o número é primo!'''
if div == 2:
    print(f'O número {num} é primo.')
else:
    print(f'O número {num} não é primo.')
