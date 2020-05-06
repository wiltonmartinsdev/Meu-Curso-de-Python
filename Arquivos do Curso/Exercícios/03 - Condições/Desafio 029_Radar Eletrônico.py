'''
1- Escreva um programa que leia a velocidade de um carro.
2- Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
3- A multa vai custar R$ 7.00 por cada Km acima do limite.

'''

velocidade = int(input('Qual a velocidade do carro em Km/h: '))
multa = (velocidade-80) * 7

if velocidade > 80:
    print('Você ultrapassou o limite de velocidade permitida e será multado! Sua multa será no valor de R$ {:.2f}.'.format(multa))
else:
    print('Velocidade atual permitida, dirija sempre com cuidado!')
