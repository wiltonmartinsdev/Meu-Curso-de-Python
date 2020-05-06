# Faça um programa que leia o peso de cinco pessoas. No final mostre qual foi o maior e menor peso lido.

maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input('Digite o peso da {}ª Pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print('\nO Maior peso foi: {} Kg! \nE o Menor peso foi: {} Kg!'.format(maior, menor))
