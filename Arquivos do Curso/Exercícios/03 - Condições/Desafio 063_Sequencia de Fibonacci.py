# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os primeiros elementos de uma sequencia de fibonacci. Ex.: 0,1,1,2,3,8
import emoji
print('{:=^50}'.format(' SEQUÊNCIA DE FIBONACCI '))
n = int(input('Quantos termos você deseja mostrar? '))
t1 = 0
t2 = 1

print('1º', t1, emoji.emojize('\033[1;34m:arrow_forward:\033[m', use_aliases=True), '2º', t2, emoji.emojize('\033[1;34m:arrow_forward:\033[m', use_aliases=True), end=' ')

cont = 3
mais = n
total = 0

while mais != 0:
    total += mais
    while cont <= total:
        t3 = t2 + t1
        print('{}º'.format(cont), t3, emoji.emojize('\033[1;34m:arrow_forward:\033[m', use_aliases=True) if cont < total else ' ', end=' ')
        t1 = t2
        t2 = t3
        cont += 1
    n1 = int(input('\nQuantos termos deseja mostrar a mais? '))
    mais = n - (n - n1)
    if n1 == 1:
        print(emoji.emojize('\033[1;34m:arrow_forward:\033[m', use_aliases=True), end=' ')
    elif n1 == 0:
        mais = 0
print('Você encerrou o programa!')
print('Foram mostrados ao todo: {} termos.'.format(cont-1))

'''
Minhas Outra Solução:

quant_termo = int(input('Quantos termos você deseja mostrar da sequência de Fibonacci: '))
t1 = 0
t2 = 1
print(t1, t2, end=' ')
mais = quant_termo
cont = 3
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        t3 = t2 + t1
        print(t3, end=' ')
        t1 = t2
        t2 = t3
        cont += 1
    mais = int(input('Deseja mostrar mais quantos termos? '))
print('Foram mostrados ao todo {} termos.'.format(cont-1))
'''