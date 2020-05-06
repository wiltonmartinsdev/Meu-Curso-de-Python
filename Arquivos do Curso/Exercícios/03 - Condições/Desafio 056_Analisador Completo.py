''' Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
1 - A média de idade do grupo.
2 - Qual o nome do homem mais velho.
3 - Quantas mulheres tem mais de 20 anos.
'''
homem_maior_idade = 0
cont_mulher = 0
soma_idade = 0

for c in range(1, 4):
    print('{:=^50}'.format(' Cadastro de Clientes '))
    print('Dados Pessoais do {}º Cliente.'.format(c))
    nome = str(input('Digite seu Nome: ')).upper() .strip()
    idade = int(input('Digite a sua Idade: '))
    sexo = str(input('Digite seu Sexo [M/F]: ')).strip()
    soma_idade += idade
    media = soma_idade/4

    if sexo in 'Mm' and idade > homem_maior_idade:
        homem_maior_idade = idade
        nome_homem_maior = nome
    elif sexo in 'Ff' and idade > 20:
        cont_mulher += 1

print('\n{:=^50}'.format(' ANALISANDO OS DADOS DO CADASTRO '))
print('A média da idade do grupo é: {}'.format(media))
print('{}, com {} anos é o nome do homem com maior idade!'.format(nome_homem_maior,homem_maior_idade))
print('{} Mulheres têm mais de 20 anos de idade!'.format(cont_mulher))
print('{:=^50}'.format(' FIM '))


