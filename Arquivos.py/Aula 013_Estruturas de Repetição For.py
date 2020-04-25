print('=-' * 20)
print('{:*^40}'.format(' EXEMPLO 01 '))

for c in range(1,6): # Irá mostrar 'oi' 5 veses.
    print('oi')
print('FIM')

print('=-' * 20)
print('{:*^40}'.format(' EXEMPLO 02 '))

for c in range(0,6): # Irá mostrar 'oi' 6 veses.
    print('oi')
print('FIM')

print('=-' * 20)
print('{:*^40}'.format(' EXEMPLO 03 '))

for c in range(0,6): # Irá mostrar 'oi' e 'fim' 6 veses.
    print('oi')
    print('FIM')

print('=-' * 20)
print('{:*^40}'.format(' EXEMPLO 04 '))

for c in range(0,6): # Irá mostrar de 0 até 5.
    print(c)
print('FIM')

print('=-' * 20)
print('{:*^40}'.format(' EXEMPLO 05 '))

for c in range(1,7): # Irá mostrar de 1 até 6.
    print(c)
print('FIM')

print('=-' * 20)
print('{:*^40}'.format(' EXEMPLO 06 '))

for c in range(6,0, -1): # Irá mostar em ordem decrescente de 6 até 1.
    print(c)
print('FIM')

print('=-' * 20)
print('{:*^40}'.format(' EXEMPLO 07 ')) 

for c in range(0,7,2):# Irá mostrar de 0 até 6 de 2 em 2.
    print(c)
print('FIM')


print('=-' * 20)
print('{:*^40}'.format(' EXEMPLO 08 ')) 

n = int(input('Digite um Número: '))
for c in range(0,n+1): # Irá mostrar de 0 até o valor de 'n'.
    print(c)
print('FIM')

print('=-' * 20)
print('{:*^40}'.format(' EXEMPLO 09 ')) 

i = int(input('Digite um valor para inicio: '))
f = int(input('Digite um valor para final: '))
p = int(input('Digite um valor para o passo: '))

for c in range(i,f+1,p): #Irá mostrar o ínicio, o fim e o passo, de acordo com os digitos informado.
    print(c)
print('FIM')


print('=-' * 20)
print('{:*^40}'.format(' EXEMPLO 10 ')) 

for c in range(0,3): # Irá repetir 'n' 3 veses.
    n = int(input('Digite um número: '))
print('Você digitou {} veses! FIM'.format(n))


print('=-' * 20)
print('{:*^40}'.format(' EXEMPLO 11 ')) 

s = 0
for c in range(0,4): # Irá mostrar a soma dos valores de 'n'.
    n = int(input('Digite um Número: '))
    s += n
print('A soma dos número digitados foi: {}'.format(s))


