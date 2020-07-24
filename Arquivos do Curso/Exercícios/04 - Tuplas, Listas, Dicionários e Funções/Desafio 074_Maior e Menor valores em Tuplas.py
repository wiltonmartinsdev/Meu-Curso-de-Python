# Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e maior valor que estão na tupla.

from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(
    1, 10), randint(1, 10), randint(1, 10))

print('Os números sorteados aleatoriamente foram:', end=' ')
for n in numeros:
    print(n, end=' ')
print(f'\n\nO maior número sorteado foi: {max(numeros)}')
print(f'O menor número sorteado foi: {min(numeros)}')
