# Faça um programa que leia um ângulo qualquer e mostre o valor na tela do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

ang = float(input('Digite um valor para o ângulo: '))
seno = sin((radians(ang)))
print('O ângulo de {}, tem o SENO de {:.2f}'.format(ang,seno))

cose = cos(radians(ang))
print('O ângulo de {}, tem o COSSENO de {:.2f}'.format(ang, cose))

tang = tan(radians(ang))
print('O ângulo de {}, tem a TANGENTE de {:.2f}'.format(ang, tang))


