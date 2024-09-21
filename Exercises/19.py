num = int(input("Informe um número: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f"Analisando o numero {num}")
print(f"unidade {u}")
print(f"Dezena {d}")
print(f"centena {c}")
print(f"milhar {m}")
