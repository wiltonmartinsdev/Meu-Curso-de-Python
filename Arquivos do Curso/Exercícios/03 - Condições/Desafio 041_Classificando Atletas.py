'''
1- A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idadde:
1.1- Até 09 anos: Mirim.
1.2- Até 14 anos: Infantil.
1.3- Até 19 anos: Júnior.
1.4- Até 20 anos: Sênior.
1.5- Acima: Master.
'''
from datetime import date
ano_atual = date.today().year

data_nasc = int(input('Digite seu ano de Nascimento para saber a sua Categoria:'))
idade_atual = ano_atual - data_nasc

if idade_atual <= 9:
    print('Com {} anos de idade, sua categoria será: MIRIM!'.format(idade_atual))
elif idade_atual <=14:
     print('Com {} anos de idade, sua categoria será: Infantil!'.format(idade_atual))
elif idade_atual <= 19:
    print('Com {} anos de idade, sua categoria será: Júnior!'.format(idade_atual))
elif idade_atual <= 20:
    print('Com {} anos de idade, sua categoria será: Sênior!'.format(idade_atual))
else:
    print('Com {} anos de idade, sua categoria será: Master!'.format(idade_atual))

