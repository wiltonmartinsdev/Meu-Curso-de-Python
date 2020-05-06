# O mesmo professor do exercicio anterior quer sortear a ordem de apresentação de trabalhos de alunos. Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada.

# O SHUFFLE irá embaralhar a lista randomicamente.

from random import shuffle

n1 = input('Digite o primeiro aluno: ')
n2 = input('Digite o segundo aluno: ')
n3 = input('Digite o terceiro aluno: ')
n4 = input('Digite o quarto aluno: ')

lista = [n1, n2, n3, n4]
shuffle(lista)

print('A Ordem de apresentação será:\n', lista )




