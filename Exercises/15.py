from random import choice

listAlunos = [] 

for i in range(4):
    alunos = input(f"Qual o nome do aluno {i+1}?")
    listAlunos.append(alunos)
sorteio = choice(listAlunos)
print(f"O aluno selecionado foi: {sorteio}")
