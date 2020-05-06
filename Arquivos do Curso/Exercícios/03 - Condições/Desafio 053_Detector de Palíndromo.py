# Crie um programa que leia uma frase qualquer e diga se ela é um políndromo, desconsiderando os espaços.

frase = str(input('Digite uma fraser qualquer: ')).strip().upper()
frase_indice = frase.split()
frase_junta = ''.join(frase_indice).strip().upper()
frase_inversa = frase[::-1]
frase_inversa_indice = frase_inversa.split()
frase_inversa_junta = ''.join(frase_inversa_indice).strip().upper()

print('A frase digitada: \033[33m{}\033[m, escrita de forma invertida fica: \033[31m{}\033[m'.format(frase, frase_inversa_junta))

if frase_inversa_junta == frase_junta:
    print('A frase é uma \033[33mPalíndromo!\033[m')
else:
    print('Esta frase \033[33mnão é um Palíndromo!\033[m')

