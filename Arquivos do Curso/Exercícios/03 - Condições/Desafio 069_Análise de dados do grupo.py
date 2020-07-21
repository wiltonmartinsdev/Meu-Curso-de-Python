'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final mostre:
1- Quantas pessoas tem mais de 18 anos.
2 - Quantos homens foram cadastrados.
3- Quantas mulheres tem menos de 20 anos.
'''
maior_18 = 0
homens_cad = 0
mulher_menor20 = 0
print('{:=^40}'.format(' CADASTRO DE PESSOAS '))
while True:
    idade = int(input('Digite a sua Idade: '))
    if idade >= 18:
        maior_18 += 1
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Digite o seu Sexo: [F/M]: ')).strip().upper()
        if sexo == 'M':
            homens_cad += 1
        if sexo == 'F' and idade <= 20:
            mulher_menor20 += 1
    resp = str(input('\nVocê deseja continuar [S/N]? ')).strip().upper()
    while resp not in 'SN':
        resp = str(input('\nValor Inválido! Você deseja continuar [S/N]? ')).strip().upper()
    if resp == 'N':
        break
print('\n{:=^55}'.format(' ANÁLISE DO CADASTRO '))    
if maior_18 > 0:
    if maior_18 == 1:
        print(f'Somente {maior_18} pessoa cadastrada é maior de 18 anos.')
    else:
        print(f'{maior_18} Pessoas cadastradas são maiores de 18 anos.')
else:
    print('\nNenhuma pessoa a partir de 18 anos foi cadastrada!') 
if homens_cad > 0:
    if homens_cad == 1:
        print('Foi cadastrado somente 1 Homem.')
    else:
        print(f'{homens_cad} Homens foram cadastrados.')
else:
    print('Não foi cadastrado nenhum homem!')
if mulher_menor20 > 0:
    if mulher_menor20 == 1:
        print('Foi cadastrada somente uma Mulher menor de 20 anos!')
    else:
        print(f'{mulher_menor20} Mulheres menores de 20 anos foram cadastradas.')
else:
    print('Não foi cadastrada nenhuma mulher!')
