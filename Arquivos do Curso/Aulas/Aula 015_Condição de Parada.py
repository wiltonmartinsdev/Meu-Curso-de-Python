'''
Nessa aula aprendir além de usar a condição Break, usar também a nova forma de usar o print. Agora utilizamos na nova versão do python o 'print formatado' (print(f'{aqui vai o nome da variável}')), 
não precisando usar mais o '.format'.
'''

n = soma = cont = 0

while True:
    n = int(input('Digite qualquer número [Digite 999, quando quiser encerrar!]:  '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Ao todo foram digitados {cont} números e a soma entre eles foi: {soma}.')

print('=-' * 35)

idade = 31
nome = 'Wilton'

print(f'Meu nome é {nome} e tenho {idade} anos!')