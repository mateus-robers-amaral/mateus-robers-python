import random
m = []
pares = []
for i in range(0,6):
    m.append([])
    for j in range(0,6):
        num = random.randint(1,50)
        m[i].append(num)
        if i == j:
            if num % 2 == 0:
                pares.append(num)
print(m)
print(pares)
