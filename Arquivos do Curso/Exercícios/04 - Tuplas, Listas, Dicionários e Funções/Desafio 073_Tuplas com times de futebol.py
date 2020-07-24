'''
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:
1- Apenas os 5 primeiros colocados.
2- Os últimos 4 colocados da tabela.
3- Uma lista com os times em ordem alfabética.
4- Em que posição da tabela esta o time da Chapecoense.
'''

times = ('Vasco', 'Sport', 'Fluminense', 'Athetico-PR', 'São Paulo',
         'Góias', 'Fortaleza', 'Bahia', 'Flamengo', 'Palmeiras', 'Corinthians', 'Atlético-GO', 'Santos', 'Coritiba', 'Atlético-MG', 'Internacional', 'Ceará', 'Botafogo', 'Grêmio', 'Chapecoense')
print('TABELA DO CAMPEONATO BRASILEIRO\n')
print(times)
print('-=' * 123)
print(f'Os 5 primeiros colocados da tabela são: {times[0:5]}')
print('-=' * 50)
print(f'Os 4 últimos colocados da tabela são: {times[-4:]}')
print('-=' * 131)
print(f'A lista dos times em ordem alfabética é: {sorted(times)}')
print('-=' * 17)
print(f'O Chapecoense esta na {times.index("Chapecoense")+1}ª Posição')
print('-=' * 17)