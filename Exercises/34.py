#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

num1 = int(input("Escreva o primeiro número: "))
num2 = int(input("Escreva o segundo número: "))

if num1 > num2:
    print(f"O número {num1} é maior que o número {num2}")
elif num2 > num1:
    print(f"O número {num2} é maior que o número {num1}")
else:
    print("Os números são iguais, tente novamente.")