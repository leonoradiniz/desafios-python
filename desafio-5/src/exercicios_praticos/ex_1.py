import random

A = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):  
    for j in range(3):  
        elemento = random.randint(1, 100)
        A[i][j] = elemento

print(A)



