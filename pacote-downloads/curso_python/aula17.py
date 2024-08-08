entrada = input('Entrar ou sair do sistema [E/S]: ')
senha_permitida = '123'
if (entrada == 'E' or entrada == 'e'):
    senha = input('Senha: ')
    if senha == senha_permitida:
        print('Você entrou no sistema.')
    elif not senha:
        print('Você não informou nenhuma senha.')
    else: 
        print('Senha incorreta. Você saiu do sistema.')
elif not entrada:
    print('Você não informou nada.')
else:
    print('Você saiu do sistema.')
