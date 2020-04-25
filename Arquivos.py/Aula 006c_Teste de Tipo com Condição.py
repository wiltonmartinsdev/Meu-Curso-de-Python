import emoji

frase = str(input('Digite algo: '))
frase.isnumeric()
resp = frase.isnumeric()

if resp == True:
    print(emoji.emojize('Foi digitado um número :1234:', use_aliases=True))
else:
    print(emoji.emojize('Foi digitada uma String :abc:', use_aliases=True))

