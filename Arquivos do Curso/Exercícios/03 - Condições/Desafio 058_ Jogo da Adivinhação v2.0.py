'''
Melhore o jogo do Desafio 028 aonde o computador vai "Pensar" em um número de 0 a 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram
necessários para vencer.
'''
from random import randint

computador = randint(0, 4)

acertou = False
cont_palpite = 0

print('{:=^91}'.format(' JOGO DA ADIVINHAÇÃO '))
print('O Computador pensará em um número entre 0 a 10 e você tentará adivinhar! Vamos começar?')


while not acertou:
    jogador = int(input('Digite um número: '))
    cont_palpite += 1
    if jogador == computador:
        acertou = True
        print('\033[1;34mVOCÊ ACERTOU!\033[m Você precisou de {} tentativas para adivinhar o número que o Computador pensou!'.format(cont_palpite))
    elif jogador > computador:
        print('\033[31mOPS, VOCÊ ERROU!\033[m O Computador pensou em um número menor. Tente Novamente!')
    else:
        print('\033[31mOPS, VOCÊ ERROU!\033[m O Computador pensou em um número maior. Tente Novamente!')
