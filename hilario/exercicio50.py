c = []
for i in range(10):
    a = []
    vetor_a = int(input(f"Digite o {i+1}° número: "))
    a.append(vetor_a)

for i in range(10):
    b = []
    vetor_b = int(input(f"Digite o {i+1}° número: "))
    b.append(vetor_b)

if vetor_a in b and vetor_b in a:
    c.append(vetor_a)
print(c)