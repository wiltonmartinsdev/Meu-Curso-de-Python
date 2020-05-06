# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, so que agora utilizando um laço for.

n = int(input('Digite um valor para a tabuada ser calculada: '))
for c in range(1,11):
    print('{}  x {:2} = {}'.format(n,c,n*c))
print('fim')
