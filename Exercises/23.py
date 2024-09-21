#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input("Escreva seu nome completo: ")).split()

print(f'Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome[0]}')
print(f'E o seu ultimo nome é {nome[-1]}')
