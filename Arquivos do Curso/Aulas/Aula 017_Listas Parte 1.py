# Listas são mutável.

print('{:=^50}'.format(' EXEMPLO 01 '))
num = [2, 5, 9, 1]
print(num)

print('{:=^50}'.format(' EXEMPLO 02 ')) # O num[2] irá substituir na posição 2 pelo valor 3.
num = [2, 5, 9, 1]
num[2] = 3
print(num)

print('{:=^50}'.format(' EXEMPLO 03 ')) # O .append() cria um novo elemento na lista
num = [2, 5, 9, 1]
num.append(7)
print(num)

print('{:=^50}'.format(' EXEMPLO 04 ')) # O .sort() irá organizar os elementos pela ordem crescente.
num = [2, 5, 9, 1, 7]
num.sort()
print(num)

print('{:=^50}'.format(' EXEMPLO 05 ')) # O .sort(reverse=True) irá organizar os elementos pela ordem decrescente.
num = [2, 5, 9, 1, 7]
num.sort(reverse=True)
print(num)

print('{:=^50}'.format(' EXEMPLO 06 '))
num = [2, 5, 9, 1, 7]
print(f'Essa lista tem {len(num)} elementos.')

print('{:=^50}'.format(' EXEMPLO 07 ')) # O .insert(2,0) irá adicionar um novo elemento, o número 0, na posição 2 reorganizando os índices.
num = [2, 5, 9, 1, 7]
num.insert(2,0)
print(num)

print('{:=^50}'.format(' EXEMPLO 08 ')) # O .pop() irá remover o último elemento da lista.
num = [2, 5, 0, 9, 1, 7]
num.pop()
print(num)

print('{:=^50}'.format(' EXEMPLO 09 ')) # O .pop(2) irá remover o elemento da posição 2.
num = [2, 5, 0, 9, 1, 7]
num.pop(2)
print(num)

print('{:=^50}'.format(' EXEMPLO 10 ')) # O .remove(2) irá remover a primeira ocorrência do número 2.
num = [7, 5, 0, 3, 2, 1]
num.insert(2, 2)
num.remove(2)
print(num)

print('{:=^61}'.format(' EXEMPLO 11 ')) # O .remove(9) com condição irá remover o número 9 se existir na lista.
num = [7, 5, 0, 3, 2, 1]
num.insert(2, 2)
if 9 in num:
    num.remove(9)
else:
    print('Não foi encontrado o número 9 na lista: ', end= '')
print(num)

print('{:=^61}'.format(' EXEMPLO 12 '))
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:
    print(f'{v}...')

print('{:=^61}'.format(' EXEMPLO 13 '))
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')

'''print('{:=^61}'.format(' EXEMPLO 14 ')) # Ler valores pelo teclado e colocar dentro da lista.
valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
'''
print('{:=^61}'.format(' EXEMPLO 15 '))
a = [2, 3, 4, 7]
b = [2, 3, 4, 7]
print(f'Lista A: {a}')
print(f'Lista B: {b}')

print('{:=^61}'.format(' EXEMPLO 16 ')) # Quando igualamos uma lista o python cria uma ligação entre elas, se alterarmos algum elemento iremos alterar nas duas listas.
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

print('{:=^61}'.format(' EXEMPLO 17 ')) # b = a[:] A lista 'b' irá receber uma cópia dos valores da lista 'a', podendo alterar algum elemento da lista 'b' que não irá alterar nenhum elemento da lista 'a'.
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

