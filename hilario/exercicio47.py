import random

a = []
for i in range(20):
    num = random.randint(1, 50)
    a.append(num)

b = []
c = []
for num in a:
    if num % 2 == 0:
        b.append(num)
    else:
        c.append(num)

print(a, b, c)