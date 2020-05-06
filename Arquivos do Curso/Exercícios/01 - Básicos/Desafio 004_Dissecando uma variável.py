# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela.

n = (input('Digite Algo: '))

print('As letras estão todas em minúsculas: ', n.islower())
print('As letras estão todas em maisúsculas: ', n.isupper())
print('É alfabético? ', n.isalpha())
print('É alfanumérico?', n.isalnum())
print('Só tem espaços? ', n.isspace())
print('Está capitalizada? ', n.istitle())
print('É um número? ', n.isnumeric())

