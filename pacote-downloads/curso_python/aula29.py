nome = 'NATHÁLIA LINDA'


c = 0
novo_nome = ''
while c < len(nome):

    letra = nome[c]
    novo_nome = novo_nome + f'*{letra}'
    c = c + 1
novo_nome = novo_nome + '*'
print(novo_nome)


