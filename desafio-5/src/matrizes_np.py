import numpy as np

# Anotação para aprendizado: aqui calcula-se a inversa da matriz, se ela for invertível.
# linalg = funções de álgebra linear no numpy
# det = calcula determinante
A = np.array([[3, 1], [2, 4]])
if np.linalg.det(A) != 0:
    inversa = np.linalg.inv(A)
    print("Inversa de A:\n", inversa)
else:
    print("Matriz não invertível.")
