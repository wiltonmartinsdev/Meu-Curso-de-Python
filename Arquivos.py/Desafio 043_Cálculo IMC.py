'''
Desenvolva uma lógica que calcule o peso e altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com a tabela abaixo:
1- Abaixo de 18.5: Abaixo do Peso!
2- Entre 18.5 e 25: Peso Ideal!
3- 25 até 30: Sobrepeso!
4- 30 a 40: Obesidade!
5- Acima de 40: Obsidade Mórbida!
'''

peso = float(input('Digite seu Peso (Kg): '))
altura = float(input('Digite sua Altura (M): '))
imc = peso / altura **2

if imc <18.5:
    print('Você está ABAIXO DO PESO! Seu IMC é: {:.1f}'.format(imc))
elif imc <=25:
    print('Você está com seu PESO IDEAL! Seu IMC é: {:.1f}'.format(imc))
elif imc <=30:
    print('Você está com SOBREPESO! Seu IMC é: {:.1f}'.format(imc))
elif imc <=40:
    print('Você está com OBESIDADE! Seu IMC é: {:.1f}'.format(imc))
else:
    print('Você está com OBESIDADE MÓRBIDA Seu IMC é: {:.1f}'.format(imc))



