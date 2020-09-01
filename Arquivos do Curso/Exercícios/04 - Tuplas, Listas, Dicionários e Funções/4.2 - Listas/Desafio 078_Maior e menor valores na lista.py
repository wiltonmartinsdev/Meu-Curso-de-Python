# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas repectivas posições na lista.
# Minha Solução verificando  as posições: Se encontrar somente uma posição mostra no singular: 'na posição', se for duas mostra no plural: 'nas posições'.  
valores = []
maior = menor = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print('-=' * 30)
print(f'Você digitou os valores {valores} na lista.')
print('-=' * 30)
if valores.count(maior) == 1:
    print(f'O Maior valor digitado foi {maior} na posição {valores.index(maior)}.')
    print('-=' * 30)
else:
    if valores.count(maior) >= 2:
        print(f'O Maior valor digitado foi {maior} nas posições', end= ' ')
    for i, v in enumerate(valores):
        if v == maior:
            print(f'{i}...', end= ' ')
    print()
if valores.count(menor) == 1:
    print('-=' * 30)
    print(f'E o Menor valor foi {menor} na posição {valores.index(menor)}.')
    print('-=' * 30)
else:
    if valores.count(menor) >= 2:
        print('-=' * 30)
        print(f'E o menor valor foi {menor} nas posições', end= ' ')
    for i, v in enumerate(valores):
        if v == menor:
            print(f'{i}...', end= ' ')

'''Exercicio resolvido pelo professor
valores = []
maior = menor = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print('-=' *35)
print(f'Você digitou os valores: {valores}')
print(f'O maior valor digitado foi {maior} nas posições', end= ' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end= ' ')
print()
print(f'O menor valor digitado foi {menor} nas posições', end= ' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end=' ')
'''