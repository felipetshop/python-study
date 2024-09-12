price = float(input("Qual o preço do produto? R$"))
desc = float(input("Quantos porcentos de desconto?"))
dc = desc / 100
finalPrice = (dc * price)

print(f"O produto que custava R${price}, na promoção com desconto de {desc}% vai custar R${price - finalPrice:.2f}")