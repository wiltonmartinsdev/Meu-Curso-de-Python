#Faça um programa que mostre a tabuada de varios números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    numero = int(input('Digite um valor para calcular a tabuada [Digite um número negativo pra encerrar!]: '))
    if numero < 0:
        break
    for c in range(1,11):
        c += 0
        print(f'{numero} x {c} = {numero*c}')
print('Você encerrou o programa! Volte Sempre.')
