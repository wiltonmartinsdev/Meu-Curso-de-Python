'''
 Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, 
 mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
 '''
boletim = list()
media = 0

while True:
    nome = str(input('Qual o seu nome? ')).upper()
    n1 = float(input('Digite a Nota 1: '))
    n2 = float(input('Digite a Nota 2: '))
    media = (n1 + n2) / 2
    boletim.append([nome, [n1,n2], media])
    resp = str(input('Você deseja continuar [S/N]? ')).upper()
    while resp not in 'SN':
        resp = str(input('Valor Inválido! Você deseja continuar [S/N]? ')).upper()
    if resp == 'N':
        break
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opcao = int(input('\nDeseja pesquisar nota de qual aluno? (999 para interromper a pesquisa): '))
    if opcao <= len(boletim)-1:
        print(f'As notas de {boletim[opcao][0]} são: {boletim[opcao][1]}')
    elif opcao > len(boletim)-1 and opcao < 999:
        print('Aluno não Cadastrado!')
    elif opcao == 999:
        print('Pesquisa Finalizada!')
        break
