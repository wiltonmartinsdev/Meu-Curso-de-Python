# Desenvolva um programa que leia o primeiro termo e a razão de uma PA, No final mostre os 10 primeiros termos dessa progressão.

print('\033[33m{:=^35}\033[m'.format(' GERADOR DE PA - v1 '))

razao = int(input('Informe a razão da PA: '))
n = int(input('Informe o primeiro termo da PA: '))
termo = n + (11 - 1) * razao
cont = 0
for c in range(n, termo, razao):
    cont += 1
    print('\033[31m{}º Posição:\033[m'.format(cont), c , '/' if cont <= 9 else '', end= ' ')
print('\033[33m\nObrigado por ultilizar o Gerador de PA.\033[m')

