'''
1- Tuplas são variáveis compostas.
2 - As tuplas são Imutáveis.
3- Sorted não altera a tupla somente mostra de forma ordenada, mantendo a tupla intacta. 
4- Para apagar um tupla da memória, podemos utilizar o comando 'del' (esse comando serve para qualquer variável dentro do python), não podendo apagar somente um item.
5 - Quando trabalhamos com números em Tuplas a ordem é fundamental. Por exemplo, A + B é != B + A. 
'''
print('{:=^56}'.format(' EXEMPLO 01 '))
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudin', 'Batata Frita')
print(lanche)

print('\n{:=^56}'.format(' EXEMPLO 02 '))
print(lanche[1])

print('\n{:=^56}'.format(' EXEMPLO 03 '))
print(lanche[-2])

print('\n{:=^56}'.format(' EXEMPLO 04 '))
print(lanche[-2])

print('\n{:=^56}'.format(' EXEMPLO 05 '))
print(lanche[1:3])

print('\n{:=^56}'.format(' EXEMPLO 06 '))
print(lanche[2:])

print('\n{:=^56}'.format(' EXEMPLO 07 '))
print(lanche[:2])

print('\n{:=^56}'.format(' EXEMPLO 08 '))
print(lanche[-2])

print('\n{:=^56}'.format(' EXEMPLO 09 '))
print(lanche[-2:])

print('\n{:=^56}'.format(' EXEMPLO 10 ')) #Forma Clássica (Senão precisar da posição)
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Eu comi para caramba :-)')

print('\n{:=^56}'.format(' EXEMPLO 11 '))
print(len(lanche))

print('\n{:=^56}'.format(' EXEMPLO 12 '))
for cont in range(0, len(lanche)):
    print(cont)

print('\n{:=^56}'.format(' EXEMPLO 13 '))
for cont in range(0, len(lanche)):
    print(lanche[cont])

print('\n{:=^56}'.format(' EXEMPLO 14 '))
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')

print('\n{:=^56}'.format(' EXEMPLO 15 ')) #Quando precisar da posição.
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

print('\n{:=^56}'.format(' EXEMPLO 16 ')) #Quando precisar da posição.
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('\n{:=^56}'.format(' EXEMPLO 17 '))
print(sorted(lanche))

print('\n{:=^56}'.format(' EXEMPLO 18 '))
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)

print('\n{:=^56}'.format(' EXEMPLO 19 '))
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)

print('\n{:=^56}'.format(' EXEMPLO 20 '))
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)

print('\n{:=^56}'.format(' EXEMPLO 21 '))
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(len(c))

print('\n{:=^56}'.format(' EXEMPLO 22 '))
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c.count(5))

print('\n{:=^56}'.format(' EXEMPLO 23 '))
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.index(2)) # Quando tem dois números iguais em sequência, o c.index() irá mostrar sempre a primeira ocorrência do número em questão.

print('\n{:=^56}'.format(' EXEMPLO 24 '))
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.index(5, 1)) # Faz a busca do número 5 a partir do índice 1.

print('\n{:=^56}'.format(' EXEMPLO 25 '))
pessoa = ('Wilton', 31, 'M', 64.5)
print(pessoa)

print('\n{:=^56}'.format(' EXEMPLO 26 '))
pessoa = ('Wilton', 31, 'M', 64.5)
del(pessoa)
print(pessoa)