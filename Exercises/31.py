#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

n1 = float(input("Primeiro segmento: "))
n2 = float(input("Segundo segmento: "))
n3 = float(input("Terceiro segmento: "))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print("Os segmentos FORMAM um triangulo")
else:
    print("Os segmentos não formam um triangulo")