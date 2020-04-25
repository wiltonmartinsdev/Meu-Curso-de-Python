# Crie um programa que leia um nome de uma pessoa e diga se ela tem 'silva' no nome.

nome = str(input('Digite seu nome Completo: ')).strip()

print('Tem o nome Silva no nome digitado? {}'.format('silva' in nome.lower()))

