dias = int(input("Quantos dias o carro foi alugado?"))
kilom = int(input("Quantos KM foram rodados?"))

vDias = dias * 60
vKm = kilom * 0.15

print(f"O valor a ser pago é: {vDias + vKm}")