# Refaça o Desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while

print('\033[33m{:=^34}\033[m'.format(' GERADOR DE PA - v2 '))

razao = int(input('Digite a Razão da PA: '))
pr_termo = int(input('Digite o primeiro termo da PA: '))
prox_termo = pr_termo
cont = 1

while cont <= 10:
   print('\033[1;34m{}º Posição:\033[m'.format(cont), prox_termo, '/' if cont <=9 else ' ', end=' ')
   prox_termo += razao
   cont += 1
print('\033[33m\nObrigado por utilizar o Gerador de PA.\033[m')