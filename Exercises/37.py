#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER
from datetime import date

nascimento = int(input("Data de nascimento do atleta: "))

ano = date.today().year
idade = ano - nascimento

print("="*30)
print(f"O atleta tem {idade} anos de idade")
print("="*30)
if idade <= 9:
    print("Ele é um atleta MIRIM")
elif idade <=14:
    print("Ele é um atleta INFANTIL")
elif idade <=19:
    print("Ele é um atleta JÚNIOR")
elif idade <=25:
    print("Ele é um atleta SÊNIOR")
else:
    print("Ele é um atleta MASTER")

