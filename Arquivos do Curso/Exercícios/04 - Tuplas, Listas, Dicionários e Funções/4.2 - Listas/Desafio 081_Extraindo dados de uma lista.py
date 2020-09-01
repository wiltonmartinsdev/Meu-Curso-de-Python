'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
1- Quantos números foram digitados.
2- A lista de valores, ordenada de forma decrescente.
3- Se o valor 5 foi digitado e está ou não na lista.
'''
lista = []
while True:
    lista.append(input('Digite um valor: '))
    resp = str(input('Você deseja continuar [S/N]? ')).upper().strip()
    while resp not in 'S/N' or resp == '':
        resp = str(input('VALOR INVÁLIDO! Você deseja continuar [S/N]? ')).upper().strip()
    if resp == 'N':
        break
print('-=' * 30)
print(f'Foram digitados {len(lista)} números.\n')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente é: {lista}\n')
lista.sort()
for i, v in enumerate(lista):
    if v == 5:
        print(f'Valor CINCO, encontrado na posição {i} da lista', end= ' ')
if 5 not in lista:
    print('Valor CINCO, não encontrado em nunhuma posição da lista!', end= ' ')
print(lista, end= ' ')

'''
Caso não precise da posição do valor 5:
if 5 in lista:
    print(
        f'O valor 5 foi digitado na lista na posição {lista.index(5)}', end=' ')
else:
    print('O valor 5 não foi encontrado na lista', end=' ')
print(lista)
print('-=' * 30)
'''