# Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

lar = float(input('Digite uma valor para a Largura em Metros: '))
alt = float(input('Digite uma valor para o altura em Metros: '))
area = lar*alt

print('A área total mede:', area,'m²')

lata_tinta = 2

l_tot = area/lata_tinta

print('Será necessário ',l_tot, 'litro(s) de tinta para pintar toda essa área.')
