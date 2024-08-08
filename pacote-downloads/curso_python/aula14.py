nome = input('Olá, qual o seu nome? ')
entrada = input(f'Bem vindo(a), {nome}. Você deseja "entrar" ou "sair" do sistema? ')

if entrada == 'entrar':
    print('Você entrou no sistema!')
elif entrada == 'sair':
    print('Você saiu do sistema.')
else:
    print('O sistema não identificou uma resposta válida.')


