''' Faça um programa que leia uma frase pelo teclado e mostre:
1- Quantas vezes aparece a letra 'a'.
2- Em que posição ela aparece pela primeira vez.
3- Em que posição ela aparece pela última vez.

'''

frase = str(input('Digite uma frase: ')).strip().upper()

print('A letra "a" apareceu {} vezes na frase digitada.'.format(frase.count('A')))
print('Começou na posição: {}.'.format(frase.find('A')+1))
print('E terminou na posição: {}.'.format(frase.rfind('A')+1))

