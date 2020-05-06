from datetime import datetime, date

hora_data_padrao = datetime.now()
data_padrao = date.today()
# Hora Formatada.
hora_sistema = hora_data_padrao.strftime('%Hh:%Mmin')

# Data Formatada.
data_sistema = data_padrao.strftime('%d/%m/%Y')

print('{:=^100}'.format(
    '\033[31m GERAÇÃO DE DIÁRIAS POUSADA FORTALEZA \033[m'))
opcao = int(input('Digite 1 para CHECK-IN ou Digite 2 para CHECK-OUT: '))

if opcao == 1:
    print('{:=^100}'.format('\033[33m Área de CHECK-IN \033[m'))
    nome = str(input('Digite o nome do cliente para realizar o seu CHECK-IN: '))
    print('Seja Bem Vindo a nossa Pousada {}! Seu CHECK-IN foi realizado com sucesso as: {} - {}'.format(nome,hora_sistema, data_sistema))

elif opcao == 2:
    print('{:=^100}'.format('\033[33m Área de CHECK-OUT \033[m'))
    nome = str(input('Informe o nome do Cliente para realizar seu CHECK-OUT: '))
    tempo = int(input('Quantos dias o cliente ficou hospedado? '))
    data_checkout_padrao = date.fromordinal(data_padrao.toordinal()+tempo)

    valor_quarto = int(input('Qual o valor do seu Quarto R$? '))

    # Data CHECKOUT Formatada.
    data_checkout = data_checkout_padrao.strftime('%d/%m/%Y')

    # Hora CKECKOUT Formatada
    hora_checkout = hora_sistema

    # Quantidade de Diárias
    diaria = data_checkout_padrao - data_padrao

    # Valor a pagar
    valor_pagar = diaria*valor_quarto

    # Valor da taxa
    valor_taxa = valor_quarto - (valor_quarto*50/100)

    if hora_sistema <= '05h:59min':
        print('{:=^100}'.format('\033[31m EXTRATO DO SEU RECIBO \033[m'))

        print('{} Diárias!\nValor Total:R$ {:.2f} Reais!'.format(diaria.days, valor_pagar.days))

        print('{:=^100}'.format('\033[33m Obrigado pela sua Preferência! Volte Sempre! \033[m'))

    elif hora_sistema <= '11h:59min':
        print('{:=^100}'.format(' EXTRATO DO SEU RECIBO '))

        print('{} Diárias!\nValor Total:R$ {:.2f} Reais!'.format(diaria.days, valor_pagar.days))

        print('{:=^100}'.format('\033[33m Obrigado pela sua Preferência! Volte Sempre! \033[m'))

    elif hora_sistema <= '17h:59min':
        print('{}, você pagará uma taxa! Seu CKECK-OUT esta fora do prazo limite da Pousada!\n'.format(nome))

        print('{:=^100}'.format('\033[31m EXTRATO DO SEU RECIBO \033[m'))

        print('{} Diárias:R$ {:.2f} Reias!\nTaxa de CHECK-OUT:R$ {:.2f} Reais! \nValor Total:R$ {:.2f} Reais!'.format(diaria.days,valor_pagar.days, valor_quarto - (valor_quarto*50/100), valor_pagar.days + (valor_quarto - (valor_quarto*50/100))))
        print('{:*^100}'.format('\033[33m Obrigado pela Preferência, Volte Sempre! \033[m'))

    elif hora_sistema <= '23h:59min':
        print('{}, você pagará uma taxa,pois, seu CKECK-OUT esta fora do prazo limite estipulado pela Pousada!\n'.format(nome))

        print('{:=^100}'.format('\033[31m EXTRATO DO SEU RECIBO \033[m'))

        print('{} Diárias:R$ {} Reais!\nTaxa de CHECK-OUT:R$ {} Reais!\nValor Total:R$ {} Reais!'.format(diaria.days,valor_pagar.days, valor_quarto, valor_pagar.days+valor_quarto))

        print('{:*^100}'.format('\033[33m Obrigado pela Preferência, Volte Sempre! \033[m'))
else:
    print('Opção Inválida, tente novamente! Digite \033[33m1 para CHECK-IN\033[m ou \033[33m2 para CHECK-OUT!\033[m')