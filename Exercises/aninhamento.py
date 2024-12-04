nome = str(input("Qual seu nome? "))

#aninhamento condicional
if nome == "Felipe":
    print("Que nome bonito!")
elif nome == "Ana" or nome == "Pedro":
    print("Que nome comum")
elif nome in "Alana Julia Jessica":
    print("Nome de mulher hmm")
else:
    print("Nome paia")

print(f"Tenha um bom dia {nome}")