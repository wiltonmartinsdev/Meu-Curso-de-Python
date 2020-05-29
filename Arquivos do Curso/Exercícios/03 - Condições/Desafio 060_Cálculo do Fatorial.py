# Faça um programa que leia um número qualquer e mostre seu fatorial. Ex.: 5! = 5.4.3.2.1
'''
==========================================
UTILIZANDO MÓDULO

from math import factorial
n = int(input('Digite um número: '))
f = factorial(n)
print(f)
==========================================
UTILIZANDO O FOR
'''
n = int(input('Digite um número: '))
f = 1

for c in range(n, 0, -1):
    print(c, end=' ')
    print('x' if c > 1 else '=', end=' ')
    f *= c
print(f)



'''n = int(input('Digite um número: '))

f = 1

while n > 0:
    print(n, end='')
    print(' x ' if n > 1 else ' = ', end='')
    f *= n
    n -= 1
print(f)
'''