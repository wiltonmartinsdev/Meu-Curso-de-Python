'''
Crie um programa que leia vários números inteiros pelo teclado. O programa so vai para quando o usuário digitar 999, que é a condição de parada. No final mostre quantos números foram digitados
e qual foi a soma entre eles (Desconsiderando a flag).
'''
n = cont = soma = 0
n = int(input('Digite um número ou 999 para encerrar o programa: ')) # Repetir o mesmo flag aqui, para ser lido fora e dentro do while, assim não ira somar com os outros valores quando digitar 999.
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número ou 999 para encerrar o programa: '))
print('\nAo todo foram digitados {} números e a soma entre eles foi: {}'.format(cont, soma))