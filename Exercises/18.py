nome = str(input("Digite seu nome completo: ")).strip()

print(f"Seu nome com tudo maíusculo fica :{nome.upper()}")
print(f"Sou nome minusculo fica: {nome.lower()}")
print(f"Seu nome tem {len(nome) - nome.count(' ')} letras")

lista = nome.split()
print(f"Seu primeito nome é {lista[0]} e tem {len(lista[0])} letras")

