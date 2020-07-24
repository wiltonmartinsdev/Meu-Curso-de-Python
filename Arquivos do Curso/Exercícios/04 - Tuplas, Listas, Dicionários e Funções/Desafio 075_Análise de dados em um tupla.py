'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
1- Quantas vezes apareceu o valor 9.
2- Em que posição foi digitado o primeiro valor 3.
3 - Quais foram os números pares.
'''
numeros = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(
    input('Digite mais um número: ')), int(input('Digite o último número: ')))
print('-=' * 23)
print(f'Os números digitados foram: {numeros}')
print('-=' * 23)
if numeros.count(9) == 1:
    print(f'O valor 9 foi digitado {numeros.count(9)} vez.')
elif numeros.count(0) > 1:
    print(f'O valor 9 foi digitado {numeros.count(9)} vezes.')
else:
    print(f'O valor 9 não foi digitado em nenhuma posição.')
print('-=' * 23)
if 3 in numeros:
    print(f'O valor 3 foi digitado na {numeros.index(3)+1}ª Posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('-=' * 23)
print('Os números pares digitados foram:', end=' ')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
