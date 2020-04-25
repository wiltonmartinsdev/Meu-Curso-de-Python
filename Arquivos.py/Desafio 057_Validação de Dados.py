# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''
RESOLUÇÃO PROFESSOR:

sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while  sexo not in 'MmFf':
    sexo = str(input('Dados Inválidos. Por Favor, informe seu sexo: )).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))

Obs.: Esse [0] vai mostrar somente a primeira letra do que for digitado!
'''

resposta = 'S'
while resposta == 'S':
        sexo = str(input('Informe seu sexo [M/F]: ')).upper().strip()
        if sexo == 'M':
            sexo = sexo.replace('M', 'MASCULINO')
            print('Sexo \033[1;34m{}\033[m cadastrado com Sucesso!'.format(sexo))
            print('{:=^48}'.format(' \033[1;33mOBRIGADO PELA SUA INFORMAÇÃO!\033[m '))
            resposta = str(input('Deseja continuar [S/N]? ')).upper().strip()
        elif sexo == 'F':
            sexo = sexo.replace('F', 'FEMININO')
            print('Sexo \033[1;35m{}\033[m cadastrado com Sucesso!'.format(sexo))
            print('{:=^48}'.format(' \033[1;33mOBRIGADO PELA SUA INFORMAÇÃO!\033[m '))
            resposta = str(input('Deseja continuar [S/N]? ')).upper().strip()
        else:
            print('\033[31mVALOR INVÁLIDO! DIGITE\033[m "\033[1;34mM\033[m" PARA \033[1;34mMASCULINO\033[m OU "\033[1;33mF\033[m" PARA \033[1;33mFEMININO.\033[m')
print('fim')
