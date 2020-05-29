
altura = float(input('Digite a Altura (cm): '))
largura = float(input('Digite a Largura (cm): '))

metro_quadrado = altura * largura

print('A altura: {} cm e a largura: {} cm'.format(altura, largura))
print('Total de Metros Quadrados a ser utilizados: {} cm'.format(metro_quadrado))

valor_metro_quadrado = int(input('Digite o Valor do Metro Quadrado R$: '))

preco_total = (metro_quadrado * valor_metro_quadrado) / 100

print('O valor total a ser pago será de: R$ {}'.format(preco_total))



