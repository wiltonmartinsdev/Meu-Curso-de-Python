'''
1 - Faça um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
1.1 - O primeiro valor é maior.
1.2 - O segundo valor é maior.
1.3 - Não existe valor maior, os dois são iguais.
'''

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1>n2:
    print('O PRIMEIRO número é MAIOR!')

elif n2>n1:
    print('O SEGUNDO número é MAIOR!')

else:
    print('Não existe número maior nem menor, os dois números são iguais!')