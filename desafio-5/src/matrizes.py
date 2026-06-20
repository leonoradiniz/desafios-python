# Anotações para aprendizado: 

# Matriz de notas de alunos - os dados de cada aluno estão em uma linha, e cada coluna tem as notas de cada aluno.
# Exemplo: 2 linhas = 2 alunos. 3 colunas = 3 notas para diferentes momentos avaliativos, para cada aluno.

notas = [
    [8.5, 7.0, 9.0],  
    [6.0, 8.5, 7.5]  
]

print("Matriz de notas:")
for linha in notas:
    print(linha)

# Acessando e manipulando elementos da matriz

print("Nota do Aluno 1 na disciplina 2:", notas[0][1])

notas[1][2] = 9.0

print("Matriz atualizada:", notas)

media_aluno1 = (notas[0][0] + notas[0][1] + notas[0][2]) / 3
print("Média do Aluno 1:", media_aluno1)

# Fazendo operações com matrizes

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

C_adicao = [[0, 0], [0, 0]]

# Anotação para aprendizado: esse loop adiciona a soma dos respectivos elementos das matrizes A e B à matriz C 
for i in range(2):  
    for j in range(2):  
        C_adicao[i][j] = A[i][j] + B[i][j]

print("Adição das matrizes:", C_adicao)

# Anotação para aprendizado: esse loop adiciona a diferença dos respectivos elementos das matrizes A e B à matriz D 
D_subtracao= [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        D_subtracao[i][j] = A[i][j] - B[i][j]

print("Subtração das matrizes (A - B):", D_subtracao)

# Observação: Para esse tipo de operação, todas as matrizes devem ter o mesmo tamanho.