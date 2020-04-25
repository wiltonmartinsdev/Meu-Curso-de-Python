# Escreva um programa que escreva a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 0.60 por dia e R$ 0.15 por KM rodado.

quant_per = float(input('Qual a quantidade percorrida do carro em KM? '))
quant_dia = int(input('Quantos dias o carro ficou alugado? '))

vlr_per = quant_per * 0.15
vlr_km = quant_dia * 60
vlr_tot = vlr_per + vlr_km

print(' O total a ser pago será R$ {:.2f}'.format(vlr_tot))

