from random import shuffle

listAlunos = [] 

for i in range(4):
    alunos = input(f"Qual o nome do aluno {i+1}?")
    listAlunos.append(alunos)

shuffle(listAlunos)
print(f"A sequencia de alunos foi: {listAlunos}")

