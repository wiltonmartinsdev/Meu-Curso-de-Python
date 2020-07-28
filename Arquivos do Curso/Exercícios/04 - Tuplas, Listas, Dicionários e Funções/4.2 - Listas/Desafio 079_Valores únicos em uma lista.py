'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número ja exista la dentro, ele não sera adicionado. No final serão exibidos todos os valores únicos
digitados, em ordem crescente.
'''
lista_numerica = []
while True:
    numeros = int(input('Digite um valor para ser adicionado a lista: '))
    if numeros not in lista_numerica:
        lista_numerica.append(numeros)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor Duplicado! Tente outro número!')
    resp = str(input('Você deseja continuar [S/N]? ')).upper()
    if resp == 'N':
        break
lista_numerica.sort()
print(f'Os valores adicionados a lista foram {lista_numerica}')