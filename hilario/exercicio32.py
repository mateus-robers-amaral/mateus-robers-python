quest = int(input('Até qual número a série de Fibonacci deve ir?\n-> '))
anterior = 0
fibonacci = 1
for i in range(quest):
    print(fibonacci, end=" ")
    anterior, fibonacci = fibonacci, fibonacci + anterior