'''
Crie um programa que leia vários números inteiros pelo teclado. O programa so vai parar quando o usuario digirar 999, que é a condição de parada. No final mostre quantos números foram digitados
e mostre a soma entre eles (desconsiderando o flag)
'''

cont = soma = 0

while True:
    numero = int(input('Digite um número [Digite 999 quando quiser parar!]: '))
    if numero == 999:
        break
    cont += 1
    soma += numero        
print('\nVocê finalizou o programa!')
print(f'Foram digitados {cont} números e a soma entre eles foi {soma};')