# Quando queremos mostrar na tela um texto grande em vez de usar vário prints, podemos usar dessa forma: print(""" """).
# O símbolo do colchetes serve para identificar uma lista.
# O Python diferencia maiúsculas de minúsculas. Por exemplo, o 'V' não é a mesma coisa que 'v'.
# Quando o Python coloca uma string na memória do computador ela não vai inteira, ela vai fatiada. Ele cria miniespaços correspondente ao tamanho da variável e cada um desses miniespaços recebe um índice que vai do zero até o número da string em questão.
# Toda string começa com númeração a partir do número 0, contando os espaços entre as palavras.
# Geralmente uma lista de string ela é imutável, mas podemos mudar ela através dos métodos, não conseguimos mudar direto nos elementos, só através de métodos.
# Uma string no seus microelementos ela é Imutável, a não ser que utilizemos uma função de transformação de string e faça uma atribuição.

'''
Exemplo de uma string imutável:

frase = 'Curso em Vídeo'
frase = frase.replace ('Python', 'Android')
print(frase)
=======================================================================================================================


Frase de exemplo: Curso em Vídeo Python - Nessa frase iremos ter 21 carecteres, sendo 20 índices (lembrando que a contagem sempre começa com 0, por isso, 20 índices).

frase = "Curso em Vídeo Python"

1- FATIAMENTO DE UMA STRING:

1- Se mandar escrever na tela, por exemplo, frase[9], o python dentro da cadeia de caracter irá identificar somente o carecter correspondente ao 9.
2 - Se mandar escrever na tela, por exemplo, frase[9:13], o python irá pegar os valores correspondentes do 9 até o 13, so que quando chega no 13 ele não conta, sempre conta até o anterior.
2.1 - No caso do exemplo acima, ele começa a contagem no 9 e termina no 13, mas desconsidera o valor do último, considerando sempre o valor anterior, no caso, o 12. Sempre é um a menos no final, mas começa exatamente no 9.
3 - Se mandar escrever na tela, por exemplo, frase[9:21], como na nossa frase de exemplo não tem o 21 e ele desconsidera o último então irá até o 20 mesmo.
4 - Se mandar escrever na tela, por exemplo, frase[9:21:2], o python irá começar no 9 e irá parar no 21 e a sua contagem será de dois em dois.
5 - Se mandar escrever na tela, por exemplo, frase[:5], quando não colocamos aonde ele deve começar ele sempre irá começar do caractere 0 e terminar no caractere 5.
6 - Se mandar escrever na tela, por exemplo, frase[15:], quando for indicado somente o início ele começará a contagem do 15 até o final.
7 - Se mandar escrever na tela, por exemplo, frase[9::3], o python irá começar do 9 até o final de três em três.


2- ANÁLISE DE UMA STRING:

1- Se mandar escrever na tela, por exemplo, len(frase), o python irá mostrar o comprimento da frase.
2 - Se mandar escrever na tela, por exemplo, frase.count('o'), o python irá contar quantas vezes aparece a letra 'o' minúsculo na frase, caso, tivesse o 'O' maiúsculo ele não contaria.
3 - Se mandar escrever na tela, por exemplo, frase.count('0',0,13), o python irá fazer uma contagem ja com fatiamento. Irá contar do 0 até o 13, desconsiderando o valor do 13.
4 - Se mandar escrever na tela, por exemplo, frase.find('deo'), o python irá mostrar quantas vezes ele encontrou 'deo' e mostrar em qual índice começou.
5 - Se mandar escrever na tela, por exemplo, frase.find('android'), o python irá verificar que não tem a string 'android' e mostrará um valor -1. Toda vez que mostrar esse valor, significa que não encontrou nada na string que esta sendo analizada.
6 - Se mandar escrever na tela, por exemplo, 'Curso' in frase, o python irá verificar se existe a palavra 'Curso' em frase, se existir mostrará o valor 'True' indicando a existência.


3- TRANSFORMAÇÃO EM UMA STRING:

1- Se mandar escrever na tela, por exemplo, frase.replace('python', 'Android'), ele vai procurar por 'Python' e irá substituir por 'Android'.
2 - Se mandar escrever na tela, por exemplo, frase.upper(), o python irá trocar todas as letras para maiúsculo e as que ja estiverem em maiúsculo ele as mantem.
3 - Se mandar escrever na tela, por exemplo, frase.lower(), o python irá trocar todas as letras para minúsculas e as que ja estiverem em minúsculos ele as mantem.
4 - Se mandar escrever na tela, por exemplo, frase.capitalize(), o python irá trocar todos os caracteres para minúsculos e so primeiro ficará em maiúsculo.
5 - Se mandar escrever na tela, por exemplo, frase.title(), o python irá analisar quantas palavras têm essa string e colocará somente a primeira letra de cada palavra em maiúsculo e demais em minúsculo.
6 - Se mandar escrever na tela, por exemplo, frase.strip(), o python irá remover todos os espaços inúteis do inicio e no final da string, permancendo o espaço entre as palavras, excluindo somente os espaços do inicio e fim.
7 - Se mandar escrever na tela, por exemplo, frase.rstrip(), o python irá remover somente os últimos espaços, se estiver espoço no inicio ele não irá remover, somente no final.
8 - Se mandar escrever na tela, por exemplo, frase.lstrip(), o python irá remover somente os primeiros espaços, se estiver espaço no final ele não irá remover, somente no inicio.


4- DIVISÃO EM STRING:

1 - Se mandar escrever na tela, por exemplo, frase.split(), no comando split() irá ocorrer uma divisão dentro da sua string considerando os espaços, e a cada nova divisão irá refazendo os índices e cada palavra recebe indexação nova.
1.1 - Técnicamente o split gera uma lista com todas as palavras de uma cadeia de caracteres e então ele separa os novos pedaços divididos e gera um índice tambem com o conjunto de palavras divididas


5- JUNÇÃO EM STRING:

1 - Para fazer a junção a string em si ja deve estar "splitada".
2 - Se mandar escrever na tela, por exemplo, '-'.join(frase), o python irá juntar todos os elementos da frase e vai usar o separador '-' entre as palavras.
'''

frase = 'Curso em Vídeo Python'
dividido = frase.split()

print(dividido[2][3])


