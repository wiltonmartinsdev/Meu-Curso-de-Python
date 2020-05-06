'''
Enunciado Exercicio 35: Desenvolva um programa que leia um comprimento de três retas e diga ao usuário se elas podem ou não fomar um triângulo.
Enunciado Exercicio 42: Refaça os Exercicio 35 dos triângulos, acrescentando o recurso que tipo de triangulo será formado:
a) Equilátero: Todos os lados são iguais.
b) Isósceles: Dois lado iguais.
c) Escaleno: Todos os lado diferentes.

Obs.: Temos que tomar cuidado ao verificar se é Escaleno, porque a igualdade é inclusiva (r1 == r2 and r2 == r3) mas na diferença não!
Exemplo: O r1 pode ser diferente de r2, r2 pode ser diferente de r3 mas o r1 pode ser igual ao r3. Então, temos que testa essa diferença.
Exemplo: r1 != r2 != r3 != r1
'''

r1 = float(input('Digite um valor para a Primeira Reta: '))
r2 = float(input('Digite um valor para a Segunda Reta: '))
r3 = float(input('Digite um valor para a Terceira Reta: '))

if r1< r2+r3 and r2< r1+r3 and r3< r1+r2:
    print('Com esses valores poderá formar um triângulo!')
    if r1 == r2 == r3:
        print('O triângulo formado é classificado como: EQUILÁTERO!')
    elif r1 == r2 != r3 or r2 == r3 != r1 or r3 == r1 != r2 :
        print("O Triângulo formado é classificado como: ISÓSCELES!")
    else:
        print('O Triângulo formado é classificado como: ESCALENO!') 
else:
    print('Com esses valores não poderá formar um triângulo!')    


