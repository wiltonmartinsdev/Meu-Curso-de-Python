'''
 Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, 
 mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
 '''
lista_completa = list()
lista_cadastro = list()
media = 0

while True:
    lista_cadastro.append(str(input('Digite seu nome: ')))
    n1 = float(input('Digite a Nota 1: '))
    lista_cadastro.append(n1)
    n2 = float(input('Digite a Nota 2: '))
    lista_cadastro.append(n2)
    media = (n1 + n2) / 2
    lista_cadastro.append(media)
    lista_completa.append(lista_cadastro[:])
    lista_cadastro.clear()
    resp = str(input('Você deseja continuar [S/N]? ')).upper()
    while resp not in 'SN':
        resp = str(input('Valor Inválido! Você deseja continuar [S/N]? ')).upper()
    if resp == 'N':
        break
print(lista_completa)
print(lista_completa[0][3])
print(f'Nota 1: {lista_completa[0][1]}')
print(f'Nota 2: {lista_completa[0][2]}')

