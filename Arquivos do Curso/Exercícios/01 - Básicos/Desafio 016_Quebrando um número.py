# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira.

''' Outra forma de fazer:

num = float(input('Digite um número: '))
print('O número digitado foi {} e sua porção inteira é: {}'.format(num, int(num)))'''

from math import trunc

num = float(input('Digite um número Real? '))

print('O número digitado foi {} e sua porção inteira é: {}'.format(num, trunc(num)))
