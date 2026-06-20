estoque = [
        [10, 5, 8],
        [3, 7, 2],
        [6, 4, 9]
        ]

precos = [
        [15.50, 10.00, 40.00],
        [100.00, 30.00, 70.00],
        [25.50, 110.00, 49.50]
        ]

valor_em_estoque = [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
                ]

for i in range(3):  
        for j in range(3):  
                valor_em_estoque[i][j] = estoque[i][j] * precos[i][j]

print(valor_em_estoque)