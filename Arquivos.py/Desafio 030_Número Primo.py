# Crie um programa que leia um número inteiro e mostre na tela se é PAR ou ÍMPAR.

num = int(input('Digite um número: '))
par = num % 2

if par == 0:
    print('O valor digitado foi o nº {} e é PAR!'.format(num))
else:
    print('O valor digitado foi o nº {} e é ÍMPAR!'.format(num))