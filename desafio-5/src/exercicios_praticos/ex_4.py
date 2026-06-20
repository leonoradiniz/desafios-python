import numpy as np

# Exemplo com matriz não invertível:
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]

if np.linalg.det(A) != 0:
    inversa = np.linalg.inv(A)
    print("Inversa de A:\n", inversa)
else:
    print("Matriz não invertível.")