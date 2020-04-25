# Escreva um programa que converta uma temperatura digitada em °C para °F.

celsius = float(input('Digite uma temperatura em °C: '))
temp_f = (celsius * 1.8) + 32

print('A temperatura digitada em °C foi: {} e convertendo para Fahrenheit fica: {:.1f}°F'.format(celsius, temp_f))