'''
Faça um programa que jogo Par ou Ímpar com o computador. O jogo se será interrompido quando o jogador perder, mostrando o total de vitórias con

'''

from random import randint

soma = 0
cont = 1
resultado = ''
computador = randint(0,11)

while True:
    jogador = int(input('Digite um número para começar a jogar: '))
    escolha = str(input('Você escolhe Par ou Ímpa? ')).upper()
    soma = jogador + computador
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'
    print(f'Você jogou {jogador} e escolheu {escolha} e o Computador jogou {computador} tendo como soma {soma}, sendo assim é {resultado}')
    if escolha != resultado:
        break
    cont += 1
print(f'Você perdeu na {cont} tentativa!')


