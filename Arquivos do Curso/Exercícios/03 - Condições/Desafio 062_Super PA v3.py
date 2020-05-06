# Melhore o desafio 061, perguntando se o usuário quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

p1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = p1
cont = 1
novo_termo = 10
total = 0

while novo_termo != 0:
    total += novo_termo
    while cont <= total:
        termo += razao
        print('\033[1;34m{}ª Posição:\033[m '.format(cont), end='')
        print(termo, end='' ' / ' if cont <= 9 else ' ')
        cont += 1
    novo_termo = int(input('\nDeseja mostrar mais quantos número? '))
print('fim')





