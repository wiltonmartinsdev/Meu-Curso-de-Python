#Crie um programa que mostre na tela todos os numeros pares que estão no intervalo entre 1 e 50.
quan = 0
for c in range(2, 51,2):
    quan += 1
    print(c,end=' ')
print('\nDos {} números da relação {} são PARES!'.format(c,quan))
