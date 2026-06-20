vendas_semana_1 = [[30], [27], [41], [12], [33], [49], [11]]
vendas_semana_2 = [[24], [38], [46], [22], [14], [31], [15]]
vendas_quinzena_por_dia = [[0], [0], [0], [0], [0], [0], [0]]

# Anotação para estudo: aqui utilizo esses valores no range pois minhas matrizes possuem 7 sublistas (linhas) cada, e cada sub-lista possui um elemento só (coluna).

# linhas → quantidade de sublistas
# colunas → quantidade de elementos dentro de cada sublista

for i in range(7):  
    for j in range(1):  
        vendas_quinzena_por_dia[i][j] = vendas_semana_1[i][j] + vendas_semana_2[i][j]
print(vendas_quinzena_por_dia)