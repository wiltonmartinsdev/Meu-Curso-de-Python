'''
Crie um programa que leia dois valores e mostre um menu na tela:

[1] Somar
[2] Multiplicar
[3] Maior Valor
[4] Novos números
[5] Sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um segundo número: '))
opcao = 0

while opcao != 5:
    print('{:=^50}'.format(' Menu de Opções '))
    print('[1] Somar.\n[2] Multiplicar.\n[3] Maior Valor.\n[4] Novos Números.\n[5] Sair do Programa.')
    print('{:=^50}'.format(''))
    opcao = int(input('O que você deseja fazer com os números digitados? '))

    if opcao == 1:
        somar = n1 + n2
        print('A soma entre {} e {}, tem como resultado: {}\n'.format(n1, n2, somar))
    elif opcao == 2:
        multiplicar = n1 * n2
        print('A multiplicação de {} x {}, tem como resultado: {}\n'.format(n1, n2, multiplicar,))
    elif opcao == 3:
        if n1 > n2:
            print('O Primeiro número: {}, é maior que o segundo número: {}\n'.format(n1, n2))
        elif n2 > n1:
            print('O segundo número: {}, é maior que o primeiro número: {} \n'.format(n2, n1))
        else:
            print('Os dois valores digitados, são iguais!\n')
    elif opcao == 4:
        print('\nDigite os números novamente!')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite um segundo número: '))
    elif opcao == 5:
        print('Você encerrou o Programa!')
    else:
        print('Opção Inválida, Tente Novamente!\n')










