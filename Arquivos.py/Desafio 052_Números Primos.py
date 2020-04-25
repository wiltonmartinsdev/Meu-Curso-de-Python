# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número: '))
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        cont += 1
        print('\033[33m', end=' ')
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')

if n == 0:
    print('Impossível dividir por {}!'.format(n))
elif n == 1:
    print('\n\033[mO número 1 não é um número primo! Porque ele tem apenas 1 divisor que é ele mesmo!')
elif cont > 2:
    print('\n\033[mO número {} foi dividido {} veses!'.format(n, cont), end=' ')
    print('Portanto não é um número primo!')
elif cont > 1 and cont == 2:
    print('\n\033[mO número {} foi dividido {} veses!'.format(n, cont), end=' ')
    print('Portanto é um número primo!')
print('fim')

