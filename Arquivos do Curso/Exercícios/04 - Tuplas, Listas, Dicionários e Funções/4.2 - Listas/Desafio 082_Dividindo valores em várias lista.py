'''
Crie um programa que vai ler vários números e colocá-los em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, 
mostre o conteúdo das três listas geradas.
'''
lista = []
lista_par = []
lista_impar = []

while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Você deseja continuar [S/N]? ')).upper().strip()
    while resp not in 'SN' or resp == '':
        resp = str(input('VALOR INVÁLIDO! Você deseja continuar [S/N]? ')).upper().strip()
    if resp == 'N':
        break
print('-=' * 30)
for i, v in enumerate(lista):
    if v % 2 == 0:
        lista_par.append(v)
    else:
        lista_impar.append(v)
print(f'Os valores digitados na lista foram {lista}')
print(f'Lista só com os valores pares {lista_par}')
print(f'Lista só com os valores Ímpares {lista_impar}')