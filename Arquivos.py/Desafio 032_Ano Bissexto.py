# Faça um programa que leia um ano qualquer e mostre se ele é Bissexto.

from datetime import date
ano = int(input('Que ano quer analizar? Digite 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano informado é BISSEXTO!')
else:
    print('O ano informado não é BISSEXTO!')