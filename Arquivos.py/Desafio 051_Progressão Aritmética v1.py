# Desenvolva um programa que leia o primeiro termo e a razão de uma PA, No final mostre os 10 primeiros termos dessa progressão.

razao = int(input('Informa a razão da PA: '))
n = int(input('Informe o primeiro termo da PA: '))
termo = n + (11 - 1) * razao
cont = 0
for c in range(n, termo, razao):
    cont += 1
    print('\033[31m{}º Posição:\033[m'.format(cont),c, end= ' / ')
print('Acabou!')

