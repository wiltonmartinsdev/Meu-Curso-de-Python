# Faça um programa em que calcule a soma entre todos os números ímpares que são multiplo de 3 e que se encontram no intervalo de 1 até 500.

quant_mult = 0
soma_mult = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma_mult += c
        quant_mult += 1
        print(c)

print('\nA soma dos {} números Ímpares e Múltiplos de 3 é: {}'.format(quant_mult,soma_mult))

