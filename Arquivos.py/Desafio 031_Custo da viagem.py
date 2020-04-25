'''
1- Desenvolva um programa que pergunte a distância de uma viagem em Km.
2- Calcule o preço da passagem cobrando R$ 0.50 por Km para viagens de até 200Km.
3- E R$ 0.45 para viagens mais longas.

'''

distancia = float(input('Qaul a distância da viagem em Km? '))

# Pode ser solucionada também usando o if simplificado que ficaria assim: preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('A distância da viagem será de {} Km e o valor da sua passagem será de R$ {:.2f}!'.format(distancia, preco))

