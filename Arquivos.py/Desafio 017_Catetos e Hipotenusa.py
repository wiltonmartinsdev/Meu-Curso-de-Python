# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

''' Outra forma de fazer:
co = float(input('Digite um valor para o Cateto Oposto: '))
ca = float(input('Digite um valor para o cateto adjacente: '))
hi = (co ** 2 + ca **2) ** (1/2)

print('A Hipotenusa vai medir  {:.2f}'.format(hi)) '''

from math import hypot

co = float(input('Digite uma valor para o Cateto Oposto: '))
ca = float(input('Digite um valor para o Cateto Adjacente: '))
hi = hypot(co, ca)

print('O valor da Hipotenusa é {:.2f}'.format(hi))

