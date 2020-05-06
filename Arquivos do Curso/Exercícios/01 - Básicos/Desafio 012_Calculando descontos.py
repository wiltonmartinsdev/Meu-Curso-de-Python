# Faça um algoritmo que leio o preço de um produto e mostre seu novo preço com 5% de desconto.

prod = float(input('Qual o valor do produto? '))
desc = float(input('Qual o valor do desconto a ser dado (%)? '))

cal_desc = (prod * desc) / 100
preco_tot = prod-cal_desc

print('O produto custa R$', prod, 'e o seu novo preço com',desc,'% de desconto é de R$',preco_tot)
