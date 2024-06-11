import random
m = []
soma = 0
for i in range(0,4):
    m.append([])
    for j in range(0,3):
        num = random.randint(1,50)
        m[i].append(num)
        soma += num
print(m)
print(soma)