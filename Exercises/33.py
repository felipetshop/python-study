#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input("Digite um número INTEIRO: "))

binary = bin (num)
hexa = hex(num)
octal = oct(num)

print("=-=" * 20)
print("CONVERSOR DE NÚMERO INTEIRO")
print("=-=" * 20)
print('''Escolha a sua Base:
[1] Para BINÁRIO
[2] Para OCTAL
[3] Para HEXADECIMAL''')

print("=-=" * 20)
sel = int(input("Selecione a sua opção:"))

if sel == 1:
    print(f"Seu número em binário ficaria {binary.lstrip('0b')}")
elif sel == 2:
    print(f"Seu número em octal ficaria {octal.lstrip('0o')}")
elif sel == 3:
    print(f"Seu número em hexadecimal ficaria {hexa.lstrip('0x')}")
else:
    print("Erro ! Você selecionou uma opção incorreta")




