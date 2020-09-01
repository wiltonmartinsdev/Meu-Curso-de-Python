# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
palpites = list()
jogos = list()
quantidade = int(input('Quantos jogos você deseja sortear? '))
total = 1
while total <= quantidade:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in palpites:
            palpites.append(num)
            cont += 1
        if cont >= 6:
            break
    palpites.sort()
    jogos.append(palpites[:])
    palpites.clear()
    total += 1
print('Processando seu jogo...')
for i, p in enumerate(jogos):
    sleep(1)
    print(f'{i+1}º Jogo: {p}')
print('Jogo Processado com Sucesso. Tenha uma Boa Sorte!')