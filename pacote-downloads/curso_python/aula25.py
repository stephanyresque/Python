"""
Repetiçoes
while (enquanto)
executa enquanto uma condição for verdadeira.
"""

cond = True
while cond:
    nome = input('Qual o seu nome? ')  # temos um exemplo de loop infinito.
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break
    
print('Acabou')
