# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Escreva uma frase: ')).strip()
frase = frase.lower()

print(f"A frase repete o A {frase.count('a')} vezes")
print(f"A letra 'A' aparece primeiro no index: {frase.find('a')+1}")
print(f"E por ultimo no index: {frase.rfind('a')+1}")
