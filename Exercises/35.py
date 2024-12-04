# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date   

nome = str(input("Qual seu nome? "))
born = int(input("Em que ano você nasceu? "))

atual = date.today()
ano = atual.year
idade = ano - born
maior = 18 - idade

print(f"Olá {nome}!!")
print("=.="*20)
print(f"Quem nasceu em {born} hoje tem {idade} anos de idade.")
print("=.="*20)

if idade >= 18:
    print("Você já fez o seu alistamento militar?")
    print("--"*20)
    print('Digite: [1] para sim  [2] para não')
    print("--"*20)
    op = int(input("Digite sua resposta: "))
    if op == 1:
        print("Tudo perfeito, tenha um ótimo dia!")
    elif op == 2:
        print(f"Você precisa URGENTEMENTE comparecer a uma unidade!")
    else:
        print("OPÇÃO INVÁLIDA, TENTE NOVAMENTE.")
else:
    print(f"Você tem {idade} anos e não precisa realizar o alistamento em {ano}.")
    print(f"Volte em {ano + maior} e faça seu alistamento.")




