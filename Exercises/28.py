num = int(input("digite um ano: "))

if (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0):
    print("Seu ano é bissexto!")
else:
    print("Seu ano não é bissexto!")
