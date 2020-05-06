# Desenvolva um programa que leia um comprimento de três retas e diga ao usuário se elas podem ou não fomar um triângulo.

r1 = float(input('Digite o valor para primeira reta: '))
r2 = float(input('Digite o valor para segunda reta: '))
r3 = float(input('Digite o valor para terceira reta: '))

if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('Os segmentos acima, podem formar um triângulo!')
else:
    print('Os segmentos acima, não podem formar um triângulo!')