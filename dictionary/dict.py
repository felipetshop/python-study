capitais = {
    "Brasil": "Brasilia",
    "Alemanha": "Berlim",
    "Japão": "Tokyo"
}

pais = input("Digite o nome do país: ")

if pais in capitais:
    capital = capitais[pais]
    print(f"A capital de {pais} é {capital}.")
else:
    print(f"A capital de {pais} não foi encontrada no banco de dados!")
