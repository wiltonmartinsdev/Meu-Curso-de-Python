# Não conseguir fazer as cores invertidas branco e preto, acho que deve ser por alguma configuração padrão do VSCODE, mas no PhyCharm conseguir normalmente!

print('====================== TESTE DE CORES - EXEMPLO 01 ======================\n')
print('\033[;;41mEssa frase esta sem estilo, na cor branca com fundo vermelho.\033[m\n')
print('\033[4;33;44mEssa frase esta em Sublinhado, na cor amarela com fundo azul.\033[m\n')
print('\033[1;35;43mEssa frase esta em negrito, com letra lilás e com fundo amarelo.\033[m\n')
print('\033[;;42mEssa frase esta sem estilo, com letra branca e com fundo verde.\033[m\n')
print('\033[mEssa frase esta com os valores padrão do terminal.\033[m\n')
print('\033[7;30;41mEssa frase esta com as cores invertidas.\033[m\n')

print('====================== TESTE DE CORES - EXEMPLO 02 ======================\n')

n1 = 2
n2 = 4

print('Os Valores são \033[32m{}\033[m e \033[31m{}\033[m!!!\n'.format(n1, n2))

print('====================== TESTE DE CORES - EXEMPLO 03 ======================\n')
nome = 'Wilton Martins'
print('Muito prazer em te conhecer, {}{}{}'.format(
    '\033[4;34m', nome, '\033[m\n'))

print('====================== TESTE DE CORES - EXEMPLO 04 ======================\n')

nome = 'Wilton Martins'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}
print('Muito prazer em te conhecer, {}{}{}'.format(
    cores['amarelo'], nome, cores['limpa']))
