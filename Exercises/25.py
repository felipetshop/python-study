velo = int(input("Qual velocidade ele estava andando? "))
multa = (velo - 80) * 7

print("=-="*20)
print(f"Você estava a {velo}KM/h")
if velo <= 80:
    print('Tudo certo! tenha um excelente dia!!')
else:
    print('Você foi multado')
    print(f'O valor da sua multa ficou no valor de {multa}R$')
print("=-="*20)
print("Favor vá até o caixa e confira as informações")
    