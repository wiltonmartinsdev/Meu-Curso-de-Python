'''
1- Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de acordo com a média atingida:
1.1- Média abaixo de 5.0: REPROVADO.
1.2- Média 5.0 e 6.9: RECUPERAÇÃO.
1.3- Média 7.0 ou superior: APROVADO. 
'''
n1 = float(input('Digite o valor da sua primeira nota: '))
n2 = float(input('Digite o valor da sua segunda nota: '))
media = (n1+n2)/2

'''if 5 <= media < 7:
    print('A sua nota final foi: {}. Você esta em RECUPERAÇÃO!'.format(media))
elif media >= 7:
    print('Asua nota final foi: {}. Você esta APROVADO(A), Parabéns!'.format(media))
elif media < 5:
    print('A sua nota final foi: {}. Você esta REPOVADO(A)!'.format(media))
'''
if media < 5:
    print('A sua nota final foi: {}. Você esta em REPROVADO!'.format(media))
elif media <= 6.99:
    print('Asua nota final foi: {}. Você esta RECUPERAÇÃO(A)!'.format(media))
elif media >= 7:
    print('A sua nota final foi: {}. Você esta APROVADO(A)!'.format(media))

