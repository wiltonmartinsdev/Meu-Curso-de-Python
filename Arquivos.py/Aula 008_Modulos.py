from math import sqrt, ceil

# 1- Quando importamos desse jeito: import math, por exemplo, estamos importando todas as funcionalidades de biblioteca.
# 2 - Quando importamos desse jeito: form import math.sqrt, por exemplo, estamos importando so a funcionalidade "sqrt".
# 2.1 - Quando importamos assim ja é importado diretamente para a pasta sem a necessidade de usar referencias, por exemplo, 'math.sqrt' ja usamos direto "sqrt()".

num = int(input('Digite um Número: '))
raiz = sqrt(num)

print('A raiz de {} é igual á {}'.format(num, ceil(raiz)))
