# Crie um programa onde o usuário possa digitar 5 valores númericos e cadastre-os em uma lista, ja na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
lista_numero = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista_numero[-1]:
        lista_numero.append(n)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        for pos in range(0, 5):
            if n <= lista_numero[pos]:
                lista_numero.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print(lista_numero)