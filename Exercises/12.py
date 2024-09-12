salary  = float(input("Qual o salário do funcionário? R$"))
upg = float(input("Quantos porcentos de aumento?"))
porcent = upg / 100
finalSalary = (porcent * salary)

print(f"O funcionario ganha R${salary}, com o aumento de {upg:.0f}% vai receber R${salary + finalSalary:.2f}")