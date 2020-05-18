'''
1- Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e pença para o usuário tentar descobrir qual foi o número escolhido pelo computador.
2- O computador deverá escrever na tela se o usário venceu ou perdeu.

Melhore o jogo do Desafio 028 aonde o computador vai "Pensar" em um número de 0 a 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram
necessários para vencer.
'''
from random import randint

computador = randint(0,2)
acertou = False
cont_jogadas = 0

while not acertou:

    jogador = int(input('Digite um número: '))
    cont_jogadas += 1
    if jogador == computador:
        acertou = True
        print('Você Acertou!')
    
    elif jogador > computador:
        print('O computador pensou em úm número menor!')
    
    else:
        print('O computador pensou em um número maior!')
print('voce preciso de {} tentativas'.format(cont_jogadas))



