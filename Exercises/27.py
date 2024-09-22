trip = int(input("Quantos Km será sua viagem? "))

if trip <= 200:
    price = 0.5 * trip
    print(f"Sua viagem é de {trip}Km, saíra no valor de {price}R$")
else:
    price = 0.45 * trip
    print(f"Por sua viagem ser de {trip}Km você ganha desconto!!")
    print(f"Sua viagem vai ser no valor de {price}R$")
print("---------------------------------------------------------")    