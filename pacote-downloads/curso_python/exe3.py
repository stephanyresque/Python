nome = input('Olá, informe seu nome: ')
tam = len(nome)

if nome:
    if tam <= 1:
        print('Tamanho mínimo de nome não foi atingido.')
    elif tam > 1 and tam <= 4:
        print('Tamanho pequeno de nome.')
    elif tam > 4 and tam <= 6:
        print('Tamanho médio de nome.')
    elif tam >6:
        print('Nome grande.')
else:
    print('Você não digitou nada.')
