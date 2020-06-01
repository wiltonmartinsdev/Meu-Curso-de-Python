'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e menor
valor lido. O programa deve perguntar ao usuário se ele quer ou não digitar valores.
'''

print('{:=^50}'.format(' MAIOR E MENOR VALOR DIGITADO '))
resp = 's'
quant_num = soma = maior = menor = 0

while resp == 's':
    numero = int(input('Digite um número: '))
    resp = str(input('Você deseja continuar [S/N]? '))
    quant_num += 1
    if quant_num == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
    soma += numero
media = soma / quant_num

print(f'\nForam digitados {quant_num} números, sendo {maior} o maior e {menor} o menor, valor digitado, sendo {soma} a soma total entre eles e tendo como média o valor de {media:.2f}.')
print('=' * 141)