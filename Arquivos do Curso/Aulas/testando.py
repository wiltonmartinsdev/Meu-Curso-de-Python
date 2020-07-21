'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário irá continuar, no final mostre:
1- Qual é o total gasto na compra.
2- Quantos produtos custam mais de R$ 1000.
3- Qual é o nome do produto mais barato.
'''
print('{:=^50}'.format(' LOJA WM INFORMÁTICA '))

compra_total = soma_preco = produto_mil = menor_preco = cont = 0
nome_menor = ' '
while True:
    produto = str(input('Digite o nome do Produto: ')).strip().upper()
    preco = float(input('Digite o valor do Produto: '))
    cont += 1
    if cont == 1:
        menor_preco = preco
        nome_menor = produto
    elif preco < menor_preco:
        menor_preco = preco
        nome_menor = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('\nVocê deseja continuar a compra [S/N]? ')).strip().upper()
    if resp == 'N':
        break

print('{:=^75}'.format(' EXTRATO DA SUA COMPRA '))
print(f'{produto}, é o produto mais barato da sua compra! Custando apenas R$ {menor_preco}')
print('-=' * 37)
print('\n{:=^75}'.format(' Obrigado pelo Preferência, Volte Sempre! '))