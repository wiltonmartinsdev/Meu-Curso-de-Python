# Crie um programa que tenha uma tupla única com nomes de produtos e seus repectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados de forma tabular.

lista = ('lápiz', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Tansferidor',
         4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('=' * 49)
print(f'{" MATERIAL ESCOLAR ":^48}')
print('=' * 49)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<40}R$ ', end='')
    else:
        print(f'{lista[pos]:>5.2f}')
print('=' * 49)
