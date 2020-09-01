nome = list()
relacao = list()
nome.append('wilton')
nome.append(31)
relacao.append(nome[:])
nome[0] = 'cesar'
nome[1] = 32
relacao.append(nome[:])
nome[0] = 'martins'
nome[1] = 30
relacao.append(nome)
print(relacao)