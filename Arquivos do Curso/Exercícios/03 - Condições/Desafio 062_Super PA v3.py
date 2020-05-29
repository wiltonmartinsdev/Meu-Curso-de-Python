# Melhore o desafio 061, perguntando se o usuário quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
print('\033[33m{:=^48}\033[m'.format(' GERADOR DE PA - v3 '))

razao = int(input('Digite um valor para a Razão da PA: '))
pr_termo = int(input('Digite um valor para o Primeiro termo da PA: '))
prox_termo = pr_termo
novo_termo = 10
cont = 1
total = 0

while novo_termo != 0:
    total += novo_termo
    while cont <= total:
        print('\033[1;34m{}ª Posição:\033[m '.format(cont), prox_termo, '/' if cont < total else '', end=' ')
        prox_termo += razao
        cont += 1
    novo_termo = int(input('\nQuantos termos a mais deseja mostrar? '))
print('\033[31mVocê encerrou! \033[33mObrigado por utilizar o Gerador de PA.\033[m')