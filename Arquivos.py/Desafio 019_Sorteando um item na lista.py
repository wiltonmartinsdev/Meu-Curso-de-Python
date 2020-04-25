# Um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

# O CHOICE escolhe um valor aleatório (randomicamente) dentro da lista.

from random import choice

n1 = input('Primeiro Aluno: ')
n2 = input('Segundo Aluno: ')
n3 = input('Terceiro Aluno: ')
n4 = input('Quarto Aluno: ')

lista = [n1, n2, n3, n4]
escolhido = choice(lista)

print('O aluno escolhido foi: {}'.format(escolhido))

