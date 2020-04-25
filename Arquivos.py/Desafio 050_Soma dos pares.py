# Desenvolva um programa que lei 6 números inteiros e mostre a soma apenas daqueles que forem par. Se o valor digitado for impar desconsidere.

'''
OUTRA FORMA!
soma = []
num_pares = 0

for x in range(1, 7):
    num = [int(input('Digite o número: '))]
    soma += [i for i in num if i % 2 == 0]
    num_pares = soma

print('\nQuantidade de pares: {}. \nSoma dos pares: {}\nOs números pares digitados foi: {}'.format(len(soma), sum(soma),num_pares))
'''

soma = 0
cont = 0
for c in range(1,7):
    n = int(input('Digite um Número: '))
    if n % 2 == 0:
        soma += n
        cont += 1

print('Ao todo, {} números pares foram digitados e a soma entre eles é: {}'.format(cont,soma))


