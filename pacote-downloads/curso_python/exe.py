nome = input('Digite o seu nome: ')
idade = input('Informe sua idade: ')


if nome and idade:
    print(f'seu nome é {nome}')
    print(f'seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços.')

    print(f'Número de caracteres: {len(nome)}')
    print(f'Primeira letra é {nome[0]}')
    print(f'Última letra é {nome[-1]}')
else:
    print('Você não informou todas as informações.')