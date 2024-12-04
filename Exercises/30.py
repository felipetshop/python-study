salary = float(input("Qual o salario do funcionario: "))

if salary <= 1250:
    aumento = (salary * 0.15) + salary
    print(f"Você vai ter um aumento de {aumento}R$")
else:
    aumento = (salary * 0.10) + salary
    print(f"Você teve um aumento de {aumento}R$")

