# Faça um programa que lei 3 números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite o Primeiro Número: '))
n2 = int(input('Digite o Segundo Número: '))
n3 = int(input('Digite o Terceiro Número: '))

# Verificando quem é o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

# Verificando quem é o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O menor número digitado foi: {}'.format(menor))
print('E o maior número digitado foi: {}'.format(maior))
