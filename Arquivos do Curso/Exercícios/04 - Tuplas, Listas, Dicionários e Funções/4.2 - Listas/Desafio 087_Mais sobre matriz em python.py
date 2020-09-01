'''Aprimore o desafio anterior, mostrando no final:
1 - A soma de todos os valores pares digitados.
2 - A soma dos valores da terceira coluna.
3 - O maior valor da segunda linha.
'''
# Minha solução:
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = []
soma = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite uma valor para a posição [{l}] [{c}]: '))
        if matriz[l][c] % 2 == 0:
            par.append(matriz[l][c])
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^4}]', end= ' ')
    print()
print(f'A Soma dos valores pares foi: {sum(par)}')
for l in range(0, 3):
    soma += matriz[l][2]
print(f'A soma dos valores na terceira coluna é: {soma}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')

'''
Solução do Professor:

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = []
soma = soma_par = maior_valor = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite uma valor para a posição [{l}] [{c}]: '))
        if matriz[l][c] % 2 == 0:
            par.append(matriz[l][c])
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^4}]', end= ' ')
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
    print()
print(f'A soma dos valores pares é: {soma_par}')
for l in range(0, 3):
    soma += matriz[l][2]
print(f'A soma dos valores na terceira coluna é: {soma}')
for c in range(0, 3):
    if matriz[1][c] > maior_valor:
        maior_valor = matriz[1][c]
print(f'O maior valor da segunda linha é: {maior_valor}')
'''