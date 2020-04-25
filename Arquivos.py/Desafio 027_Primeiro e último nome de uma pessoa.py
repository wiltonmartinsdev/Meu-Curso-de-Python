''' Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Exemplo:
Ana Maria de Souza
Primeiro: Ana.
Último: Souza

'''

nome = str(input('Digite seu nome completo: '))
print('O nome digitado foi: {}'.format(nome))

div_nome = nome.split()
print('O seu Primeiro nome é: {}.'.format(div_nome[0]))
print('E o seu Último nome é: {}.'.format(div_nome[len(div_nome)-1]))