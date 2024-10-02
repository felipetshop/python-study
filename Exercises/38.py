#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida

peso = int(input("Qual o seu peso: "))
altura = float(input("Qual sua altura: "))

imc = peso / altura**2
print(f"Seu IMC é {imc:.2f}")

if imc <=18.5:
    print("Você está abaixo do peso")
elif imc <=25:
    print("Você está no peso ideal")
elif imc <=30:
    print("Você está com sobrepeso")
elif imc <=40:
    print("Você está com obesidade")
else:
    print("Você está com obesidade mórbida CUIDADO!")