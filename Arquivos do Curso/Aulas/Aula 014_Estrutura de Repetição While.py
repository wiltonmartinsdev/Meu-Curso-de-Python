'''for c in range(1,10):
    print(c, end=' ')
print('fim')

1 - Quando escrevemos a condição, por exemplo, n != 0 esse termo chamamos de FLAG, que é a condição de parada do while. Quando digitarmos o valor ZERO o programa encerra, enquanto for diferente de ZERO o programa ficará no loop.
'''

print('{:=^50}'.format(' Primeiro Exemplo '))

c = 1
while c < 10:
    print(c, end=' ')
    c += 1
print('fim\n')


print('{:=^50}'.format(' Segundo Exemplo '))

n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('fim\n')


print('{:=^50}'.format(' Terceiro Exemplo '))

r = 's'
while r == 's':
    n = int(input('Digite um valor: '))
    r  = str(input('Deseja continuar [S/N]? '))
print('fim\n')


print('{:=^50}'.format(' Quarto Exemplo '))

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números Pares e {} números Ímpares.'.format(par, impar))
