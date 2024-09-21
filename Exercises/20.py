#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

city = str(input("Em que cidade você nasceu? ")).strip()
print(f"Sua cidade tem Santo? {'SANTO' in city.upper()}")



