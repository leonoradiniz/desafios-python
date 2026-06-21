# Criação de matriz com a biblioteca NumPy (np)

import numpy as np

min_valor = 0
max_valor = 10

matriz = np.random.randint(min_valor, max_valor, size=(3, 3))

print(matriz)