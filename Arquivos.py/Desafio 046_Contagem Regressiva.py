import emoji
from time import sleep

print('Contagem Regressiva para o Ano Novo!')

for c in range(10,0,-1):
    sleep(1)
    print(c)
sleep(1)
print(emoji.emojize('Feliz Ano Novo :sparkler: :boom: :sparkler:', use_aliases = True))



