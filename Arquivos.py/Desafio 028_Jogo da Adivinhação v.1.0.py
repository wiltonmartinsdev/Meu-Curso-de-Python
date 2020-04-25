'''
1- Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e pença para o usuário tentar descobrir qual foi o número escolhido pelo computador.
2- O computador deverá escrever na tela se o usário venceu ou perdeu.

'''

# O método leep faz o computador hibernar por alguns segundos.

from random import randint
from time import sleep

computador = randint(0, 5)
num = int(input('Que número eu pensei? '))
print('PROCESSANDO...')
sleep(1)

if num == computador:
    print('PARABÉNS, você conseguiu me vencer!')
else:
    print('O computador ganhou! ele pensou no número {} e você pensou no número {}!'. format(computador, num))


