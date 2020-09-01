# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
expressao = str(input('Digite uma expressão matemática: ')).strip()
while expressao == '':
    expressao = str(input('EXPRESSÃO INVÁLIDA! Digite uma expressão válida: ')).strip()
pilha = []
for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('EXPRESSÃO VÁLIDA!')
else:
    print('EXPRESSÃO INVÁLIDA')

