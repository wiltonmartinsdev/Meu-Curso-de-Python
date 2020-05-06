'''
1 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
1.1 - Para salários superiores a R$ 1250,00, calcule um aumento de 10%.
1.2 - Para os inferiores ou iguais, o aumento será de 15%.
'''
salario = float(input('Qual o valor do salário do funcionário R$: '))

if salario <= 1250:
    novo_salario = salario + (salario * 15 / 100)
else:
    novo_salario = salario + (salario * 10 / 100)

print('Quem ganhava R$ {} passará a ganhar R$ {}'.format(salario, novo_salario))

