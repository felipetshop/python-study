#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

print("=-="*20)
print("CONSEGUE ACERTAR O NUMERO QUE A MAQUINA ESCOLHEU?")
print("=-="*20)
choose = int(input("Qual numero você escolhe? entre 0 e 5: "))
num = randint(1, 5)
print("PROCESSANDO...")
sleep(2)
print("-------------------------------------------------")
print(f"Você escolheu o numero {choose}")
if choose == num:
    print("Parábens, você acertou o numero da maquina")
else:
    print("Você errou :( tente novamente.")
    print(f"O numero que a maquina escolheu foi: {num}")
print("-------------------------------------------------")