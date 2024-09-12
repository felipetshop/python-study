from math import sqrt

n = int(input("Digite um numero: "))
n2 = n*2
n3 = n*3
n4 = sqrt (n)

print(f"O dobro de {n} é: {n2}")
print(f"O triplo de {n} é: {n3} ")
print("A raiz quadrada de {} é : {:.2f}".format(n, n4))
