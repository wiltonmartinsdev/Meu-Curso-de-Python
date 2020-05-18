n = 1
par = impar = 0 
while n != 0:
     n = int(input('Digite um número: '))
     if n != 0:
          if n % 2 == 0:
               par += 1
          else:
               impar += 1

if par == 1 and impar == 1:
     print('Foi digitado {} número PAR e {} número ÍMPAR.'.format(par, impar))

elif par > 1 and impar == 1:
     print('Foram digitados {} números PARES e {} número ÍMPAR.'.format(par, impar))

elif impar > 1 and par == 1:
     print('Foram digitados {} números ÍMPARES e {} número PAR.'.format(impar, par))

else:
     print('Foram digitados {} números PARES e {} números ÍMPARES!'.format(par, impar))