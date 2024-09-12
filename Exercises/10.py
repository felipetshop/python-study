largura = float(input("Largura da parede em M: "))
altura = float(input("Altura da parede em M: "))

m2 = float(largura * altura) 
tinta = m2 / 2

print(f"Sua parede tem dimensão de {largura:.2f}X{altura:.2f} e a sua área é de {m2:.3f}m².")
print(f"Para pintar sua parede vai precisar de {tinta:.2f}L de tinta")