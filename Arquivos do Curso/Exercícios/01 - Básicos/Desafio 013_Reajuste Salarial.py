# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

sal = float(input('Quanto o funcionário ganha? '))
acrs_sal = float(input('Quantos % o funcionário ganhará no seu salário? '))

cal_acrs = (sal * acrs_sal) / 100
nv_sal = sal + cal_acrs

print('O funcionário ganha R$', sal, 'e o seu novo salário com', acrs_sal, '% de acréscimo será de R$:',nv_sal)

