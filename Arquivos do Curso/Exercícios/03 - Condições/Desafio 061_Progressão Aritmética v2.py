# Refaça o Desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while

p1 = int(input('Informe o Primeiro termo da PA: '))
razao = int(input('Informa a razão da PA: '))
termo = p1
c = 1


while c <= 10:
   termo += razao
   print('\033[1;34m{}ª Posição:\033[m '.format(c), end='')
   print(termo, end=' ' ' / ' if c <= 9 else ' ')
   c += 1
