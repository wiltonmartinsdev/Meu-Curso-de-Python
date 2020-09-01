print('{:=^50}'.format(' EXEMPLO 01 '))
teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)

print('{:=^50}'.format(' EXEMPLO 02'))
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste)
print(galera)

print('{:=^50}'.format(' EXEMPLO 03 ')) # Nesse exemplo foi feita uma ligação da tabela.
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)

print('{:=^50}'.format(' EXEMPLO 04 ')) # Nesse exemplo foi feita uma cópia da tabela.
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

print('{:=^50}'.format(' EXEMPLO 05 '))
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)

print('{:=^50}'.format(' EXEMPLO 06 '))
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[0])

print('{:=^50}'.format(' EXEMPLO 07 '))
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[0][0])

print('{:=^50}'.format(' EXEMPLO 08 '))
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[2][1])

print('{:=^50}'.format(' EXEMPLO 09 '))
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(p)

print('{:=^50}'.format(' EXEMPLO 10 '))
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(p[0])

print('{:=^50}'.format(' EXEMPLO 11 '))
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(p[1])

print('{:=^50}'.format(' EXEMPLO 12 '))
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')

print('{:=^50}'.format(' EXEMPLO 13 '))
galera = list()
dado = list() # Irá pegar temporariamente os dados da lista galera.
for c in range(0, 3):
    dado.append(str(input('Digite seu nome: ')))
    dado.append(int(input('Digite sua Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)

print('{:=^50}'.format(' EXEMPLO 14 '))
galera = list()
dado = list()
maior_idade = menor_idade = 0
for c in range(0, 3):
    dado.append(str(input('Digite seu nome: ')))
    dado.append(int(input('Digite sua Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        maior_idade += 1
        print('-=' * 30)
        print(f'{p[0]} é maior de Idade')
    else:
        menor_idade += 1
        print('-=' * 30)
        print(f'{p[0]} é menor de Idade')
        print('-=' * 30)
print(f'Temos {maior_idade} pessoas maiores de idade e {menor_idade} menores de idade')
print('-=' * 30)


