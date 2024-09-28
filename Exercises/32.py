#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
#o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
nome = str(input("Qual o seu nome: "))
casa = float(input("Qual o valor da casa desejada? R$: "))
salary = float(input("Qual o seu salário? R$: "))
parc = int(input("Em quantos anos você deseja quitar a casa? "))

valParc = casa / (parc * 12)
valorMax = salary * 0.3
valorEx = valorMax + salary

print(".-." * 20)
print(f"Prazer {nome}!! vamos calcular seu empréstimo")
print(".-." * 20)

print(f"A casa no valor de {casa} R$, ficaria com as parcelas no valor de {valParc:.2f} R$")
if valParc >= valorMax:
    print("Seu empréstimo foi negado!")
    print(f"Infelizmente com sua renda de {salary} R$ não é possivel fazer o empréstimo")
    print(f"Precisaria de um salário de no minimo R${valorEx}")
else:
    print("Seu empréstimo foi aprovado!!")
