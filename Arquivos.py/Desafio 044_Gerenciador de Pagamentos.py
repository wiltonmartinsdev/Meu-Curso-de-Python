'''
Elabora um programa que calcule o valor a ser pago por um produto considerando o seu Preço Normal e Condição de Pagamento:
1- A vista dinheiro ou cheque com 10% de desconto.
2- A vista no cartão com 5% de desconto.
3- Em até 2x no cartão: Preço Normal.
4- 3x ou mais no cartão: 20% de juros. 
'''

preco_produto = float(input('Qual o preço do produto desejado: R$ '))

#OPÇÕES DE PAGAMENTO
print('Digite 1 para: Pagamento A Vista no dinheiro ou Cheque com 10% de desconto.')
print('Digite 2 para: Pagamento A Vista no Cartão com 5% de desconto.')
print('Digite 3 para: Pagamento Em até 2x no Cartão com Preço Normal.')
print('Digite 4 para: Pagamento Em 3x ou Mais no Cartão com 20% de Juros.')

#OPÇÕES DE PARCELAS
print('{:=^75}'.format(' OPÇÕES DE PARCELAS '))
forma_pagamento = int(input('\nEscolha conforme as opções acima a sua forma de pagamento: '))

#condições
if forma_pagamento == 1:
    print('O produto custa R$ {} com essa forma de pagamento ficará por R$ {} com 10% de desconto!'.format(preco_produto, preco_produto - (preco_produto*10/100)))
elif forma_pagamento == 2:
    print('O produto custa R$ {} com essa forma de pagamento ficará por R$ {} com 5% de desconto!'.format(preco_produto, preco_produto - (preco_produto*5/100)))
elif forma_pagamento == 3:
    parcela = preco_produto / 2
    print('Com essa forma de Pagamento seu produto ficará com preço normal de R$ {} com 2 Parcelas no valor de R$ {} cada uma e Sem Juros!'.format(preco_produto, parcela))
elif forma_pagamento == 4:
    parcela2 = int(input('Em quantas parcelas deseja comprar em 3 ou em mais parcelas? '))
    if parcela2 == 3:
        valor_juros = preco_produto + (preco_produto *20/100)
        valor_parcela = valor_juros / parcela2 
        print('\nO produto custa R$ {} com 20% de Juros com valor final de R$ {} em {} parcelas de R$ {} cada!'.format(preco_produto,valor_juros, parcela2,valor_parcela))
    else:
        valor_juros = preco_produto + (preco_produto *20/100)
        valor_parcela = valor_juros / parcela2 
        print('\nO produto custa R$ {} parcelado em {} veses de R$ {} cada parcela. O valor final com 20% de Juros ficará R$ {}'.format(preco_produto,parcela2,valor_parcela,valor_juros))
else:
    print('Opção Incorreta, Tente Novamente com opções de 1 a 4!')
