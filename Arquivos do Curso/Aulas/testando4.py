'''Aprimore o desafio anterior, mostrando no final:
1 - A soma de todos os valores pares digitados.
2 - A soma dos valores da terceira coluna.
3 - O maior valor da segunda linha.
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = soma_terceira = maior_valor = soma_valor = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}] [{c}]: '))
        soma_valor += matriz[l][c]    
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^4}]', end=' ')
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
    print()
print(f'A soma de todos os valores pares digitados é: {soma_par}')

for l in range(0, 3):
    soma_terceira += matriz[l][2]
print(f'A soma dos valores da terceira coluna é: {soma_terceira}')

for c in range(0, 3):
    if matriz[1][c] > maior_valor:
        maior_valor = matriz[1][c]
print(f'O maior valor da segunda linha é: {maior_valor}')
print(f'A soma de todos os valores é: {soma_valor}')