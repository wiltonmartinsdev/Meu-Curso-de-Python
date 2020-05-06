# Usamos o '{:>10}' faço o alinhamento de 10 espaços para a direita ou '{:<10}' faço o alinhamento de 10 espaços para a esquerda.
# Podemos usar também o '{:^20}' irá centralizar o nome em 20 espaços.
# Podemos usar também o '{:=^20}' irá centralizar o nome entre os 20 espaços.
# Quando usamos dois prints um em baixo do outro e não queremos a quebra de linha podemo usar: end='' assim ele vai dar continuidade na linha.
# E quando queremos forçar a quebra de linha usamos: \n.

nome = input('Qual o seu nome? ')
print('Muito prazer {:=^20}!'.format(nome))

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2

print('Os números digitados foram:', n1, 'e', n2,'.', 'A soma dos números digitados é {}, sua multiplicação é {}, sua divisão é {:.2f}, sua divisão inteira é {} e sua potência é: {}'.format(s,m,d,di,e))


