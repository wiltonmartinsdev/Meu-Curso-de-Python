'''
1 - Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa.
1.1 - O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
1.2 - Calcule o valo da prestação mensal, sabendo que ele não pode exceder 30% do salário ou então o empréstimo será negado.
'''

print('==================== Calculando o Financiamento da sua Casa ====================')

valor_casa = float(input('Qual o valor da Casa R$? '))
sal_comprador = float(input('Qual o salário do Comprador R$? '))
quant_anos = int(input('Seu financiamento será em quantos anos? '))
valor_prestacao = valor_casa / (quant_anos*12)

print('Para pagar uma Casa de R$ {} em {} anos, a prestação será de R$ {:.2f}'.format(valor_casa, quant_anos, valor_prestacao))

if valor_prestacao <= sal_comprador - (sal_comprador * 30/100):
    print('Parabéns, seu financiamento foi APROVADO!')

else:
    print('Infelizmento seu financiamento NÃO FOI APROVADO! Tente novamente daqui há um 1 mês!')
