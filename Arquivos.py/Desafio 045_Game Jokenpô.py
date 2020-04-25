# crie um programa que faço o computador jogar Jokenpô.
from random import randint
from time import sleep

opcao = ('Pedra','Papel','Tesoura')
computador = randint(0,2)

print('''
Digite 0 para: Pedra.
Digite 1 para: Papel.
Digite 2 para: Tesoura: ''')

jogador = int(input('Qual opção você deseja, Pedra, Papel ou Tesoura? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!') 

if 0 <= jogador <= 2:
    if computador == 0:
        if jogador == 0:
            print('Jogo Empatado, Tente Novamente!')
        elif jogador == 1:
            print('VOCÊ VENCEU! Você jogou {} e o Computador jogou {}. O {} cobre a {}!'.format(opcao[jogador],opcao[computador],opcao[jogador],opcao[computador]))
        else:
            print('O COMPUTADOR VENCEU! O Computador jogou {} e Você jogou {}. A {} quebra a {}!'.format(opcao[computador],opcao[jogador],opcao[computador],opcao[jogador]))
    elif computador == 1:
        if jogador == 0:
            print('O COMPUTADOR VENCEU! O Computador jogou {} e Você jogou {}. O {} cobre a {}!'.format(opcao[computador],opcao[jogador],opcao[computador],opcao[jogador]))
        elif jogador == 1:
            print('Jogo Empatado, Tente Novamente!')
        else:
            print('VOCÊ VENCEU! Você jogou {} e o Computador jogou {}. A {} corta o {}!'.format(opcao[jogador],opcao[computador],opcao[jogador],opcao[computador]))
    elif computador == 2:
        if jogador == 0:
            print('VOCÊ GANHOU! Você jogou {} e o Computador jogou {}. A {} quebra a {}!'.format(opcao[jogador],opcao[computador],opcao[jogador],opcao[computador]))
        elif jogador == 1:
            print('O COMPUTADOR GANHOU! O Computador jogou {} e você jogou {}. A {} corta o {}!'.format(opcao[computador],opcao[jogador],opcao[computador],opcao[jogador]))
        else:
            print('Jogo Empatado, Tente Novamente!')
else:
    print('OPÇÃO INVÁLIDA! Você digitou {}. Tente as Opções entre 0 e 2!'.format(jogador))