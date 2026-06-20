import numpy as np

notas_alunos = [
    [8.5, 7.0, 9.0],  
    [6.0, 8.5, 7.5],
    [9.7, 4.8, 7.5],
    [6.6, 7.2, 8.0],
    [8.9, 9.2, 8.3]
    ]

medias_por_aluno = (np.mean(notas_alunos, axis=1))
medias_arredondadas = np.round(medias_por_aluno, decimals=2)
print(medias_arredondadas)

# Anotação para aprendizado: 
# Funções que retornam um valor precisam ser armazenadas — elas não modificam o valor original!