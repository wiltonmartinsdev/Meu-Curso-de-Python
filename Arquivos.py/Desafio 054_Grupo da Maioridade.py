# Crie um programa que leia o ano de nascimento de 7 pessoas, no final mostre quantas pessoas ainda não atingiram a maioridade e quantas ja são maiores.
from datetime import date

data_atual = date.today().year
cont_maior = 0
cont_menor = 0

for c in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade_atual = int(data_atual) - ano
    if idade_atual >= 21:
        cont_maior += 1
    else:
        cont_menor += 1
print('\033[33m{} Pessoas têm maior Idade\033[m e \033[31m{} Pessoas são menores de Idade\033[m'.format(cont_maior, cont_menor))
