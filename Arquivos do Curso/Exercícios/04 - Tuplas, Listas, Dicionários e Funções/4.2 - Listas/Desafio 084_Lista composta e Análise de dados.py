'''
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
1- Quantas pessoas foram cadastradas.
2- Uma listagem com as pessoas mais pesadas.
3- Uma lista com as pessoas mais leves.
'''
relacao = list()
lista_completa = list()
maior_peso = menor_peso = 0
while True:
    relacao.append(str(input('Digite seu nome: ')))
    relacao.append(float(input('Digite peso: ')))
    lista_completa.append(relacao[:])
    relacao.clear()
    resp = str(input('Você deseja continuar [S/N]? ')).upper().strip()
    while resp not in 'SN' or resp == '':
        resp = str(input('VALOR INVÁLIDO! Você deseja continuar [S/N]? ')).upper().strip()
    if resp == 'N':
        break
print('-=' * 30)
print(f'Ao todo {len(lista_completa)} pessoas foram cadastradas!')
print(f'lista completa {lista_completa}')
for i, p in enumerate(lista_completa):
    if i == 0:
        maior_peso = menor_peso = p[1]
    elif p[1] > maior_peso:
        maior_peso = p[1]
    elif p[1] < menor_peso:
        menor_peso = p[1]
print(f'O Maior peso registrado foi {maior_peso} Kg. Peso de', end=' ')
for p in lista_completa:
    if p[1] == maior_peso:
        print(f'[{p[0]}]'.upper(), end=' ')
print()
print(f'E o menor peso foi {menor_peso} Kg. Peso de', end=' ')
for p in lista_completa:
    if p[1] == menor_peso:
        print(f'[{p[0]}]'.upper(), end=' ')