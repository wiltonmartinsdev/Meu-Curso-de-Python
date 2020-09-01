# Crie um programa onde um usuário possa digitar 7 valores numéricos e cadastre-os em uma lista única que mantenha separado os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
lista_numerica = [[], []]
valor = 0
for c in range(1, 9):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        lista_numerica[0].append(valor)
    else:
        lista_numerica[1].append(valor)
lista_numerica[0].sort()
lista_numerica[1].sort()
print(f'Os valores Pares digitados foram: {lista_numerica[0]}')
print(f'E os valores ímpares foram: {lista_numerica[1]}')