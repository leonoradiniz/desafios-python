alunos = ["Mariana Silva", "Joaquim Santos", "Daniel Rodrigues", "Rafaela Pereira", "Ana Gomes"];
notas = [9.7, 6.5, 8.9, 5.2, 4.0]

notasAlunos = []

for aluno, nota in zip(alunos, notas):
    notasAlunos.append(aluno)
    notasAlunos.append(nota)


print(f"Lista de alunos: {alunos}")
print(f"Lista de notas: {notas}")
print(f"Lista de alunos e suas respectivas notas: {notasAlunos}")

print(f"Primeiro aluno: {notasAlunos[0]}")
print(f"Última nota: {notasAlunos[-1]}")
print(f"Dados dos alunos reprovados:{notasAlunos[-4:]}")

print("Nomes de todos os alunos:")
for aluno in alunos: 
    print(f"{aluno}")

i = 0

while i < len(alunos):
    print(f"Aluno no índice {i}: {alunos[i]}")
    i += 1

notasAlunos.append("Carlos Santos")
notasAlunos.append(7.8)

print(f"Dados do novo aluno: {notasAlunos[-2:]}")

notasAlunos.remove("Mariana Silva")
notasAlunos.remove(9.7)

print(f"Dados sem a primeira aluna: {notasAlunos}")

notas[3] = 6.0
notasAlunos[5] = 6.0

print(f"Nota alterada de uma aluna: {notas[3]}")

novaAluna = ["Joana Nascimento", 8.2]
notasAlunosAtualizada = notasAlunos + novaAluna

print(f"Lista de alunos e notas atualizada: {notasAlunosAtualizada}")