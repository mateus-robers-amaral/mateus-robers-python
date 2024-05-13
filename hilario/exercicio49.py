numeros = []
for i in range(20):
    num = int(input(f"Digite o {i+1}° número: "))
    
for i in range(10):
    numeros[i], numeros[i + 10] = numeros[i + 10], numeros[i]

print(f'nova lista: {numeros}')
