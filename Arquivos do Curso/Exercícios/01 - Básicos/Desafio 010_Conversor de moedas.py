# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

din = float(input('Quanto você tem em sua carteira em R$? '))
dolar = float(3.27)

print('Com R$', din, 'você pode comprar US$ {:.2f}'.format(din / dolar))
