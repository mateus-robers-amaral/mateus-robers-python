# M = [0] * 2
# for i in range(2):
#     M[i] = [0] * 3
#     for j in range(3):
#         M[i][j] = 1

# M = [[1,2,3],[4,5,6]]
# for i in range(0, 2):
#     for j in range(0, 3):
#         print('[{:^3}] '.format(M[i][j]), end='')
#     print()

# M = []
# for i in range(0,2):
#     M.append([])
#     for j in range(0,3):
#         M[i].append(int(input(f'Digite o valor [{i}][{j}]\n-> ')))
# print(M)

import random
M =[]
for i in range(0,2):
    M.append([])
    for j in range(0,3):
        M[i].append(random.randint(1,50))
print(M)
