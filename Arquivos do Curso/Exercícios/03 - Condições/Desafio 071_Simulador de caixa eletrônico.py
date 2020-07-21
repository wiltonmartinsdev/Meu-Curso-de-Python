'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
Obs.: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10, R$ 1.
'''
print('{:=^50}'.format(' BEM VINDO AO TECBANK '))
dinheiro = int(input('Quanto você deseja sacar? R$ '))
total = dinheiro
cedula = 50
total_cedula = 0

while True:
    if total >= cedula:
        total -= cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Sairam {total_cedula} Cédulas de R$ {cedula:.2f}!\n')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if total == 0:
            break
print('=' * 50)
print(f'Obrigado por utilizar o TECBANK, Volte Sempre!')
print('=' * 50)