''' Crie um programa que leia um nome completo de uma pessoa e mostre:
1- O nome com todas as letras maiúsculas e minúsculas.
2- Quantas letras no total (sem considerar espaços).
3- Quantas letras tem o primeiro nome.
'''

nome = str(input('Digite seu nome Completo: ')).strip()

print('Analisando seu nome...\n')
print('Seu nome em maiúsculas é: {}.'.format(nome.upper()))
print('Seu nome em minúsculas é: {}.'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))

separa = nome.split()

# Outra forma: print('Seu primeiro nome tem {} letras'.format(nome.fin(' ')))
print('Seu primeiro nome é {} e tem {} letras.'.format(separa[0], len(separa[0])))


