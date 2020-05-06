'''
1 - Faça um programa que leia o ano de nascimento de uma jovem e informe de acordo com sua idade:
1.1 - Se ele ainda vai se alistar ao serviço militar.
1.2 - Se é hora de se alistar.
1.3 - Se ja passou do tempo de alistamento.
1.4 - Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

from datetime import date
data_sis = date.today().year

sexo = str(input('Digite o seu Sexo (M/F): ').title().strip())

if sexo == 'Feminino':
    sim_nao = int(input('Você não tem a obrigatoriedade no Alistamento Militar! Mas mesmo assim, você gostaria de fazer seu Alistamento? Digite 1 para SIM e 2 para NÃO: '))
    if sim_nao == 2:
        print('Você esta dispensada do Serviço Militar Brasileiro!')
    elif sim_nao == 1:
        ano_nasc = int(input('Informe o ano do seu nascimento para o Alistamento Militar: '))
        calc_alist = data_sis - ano_nasc
        if calc_alist < 18:
            print('Ainda falta(m) {} ano(s) para o seu Alistamento Militar! Seu alistamento será no ano de {}!'.format(18-calc_alist, 18+ano_nasc))
        elif calc_alist == 18:
            print('Procure uma Junta Militar mais próxima de sua residência! Está no período do seu Alistamento Militar!')
        else:
            print('Você ja deveria ter se alistado há {} ano(s), seu Alistameto Militar foi em {}.'.format(calc_alist-18, ano_nasc+18))
elif sexo == 'Masculino':
    ano_nasc = int(input('Informe o ano do seu nascimento para o Alistamento Militar: '))
    calc_alist = data_sis - ano_nasc
    if calc_alist < 18:
        print('Ainda falta(m) {} ano(s) para o seu Alistamento Militar! Seu alistamento será no ano de {}!'.format(18-calc_alist, 18+ano_nasc))
    elif calc_alist == 18:
        print('Procure uma Junta Militar mais próxima de sua residência! Está no período do seu Alistamento Militar!')
    else:
        print('Você ja deveria ter se alistado há {} ano(s), seu Alistameto Militar foi em {}.'.format(calc_alist-18, ano_nasc+18))

