# CALCULADORA

print('---------CALCULADORA BÁSICA---------')
server = input('Informe seu nome: ')
print(f'Olá, {server}')
while True:

    n1 = input('informe o 1º número: ')
    n2 = input('Informe o 2º número: ')

    opr = input('Deseja trabalhar com qual operação [+/-/*//]? ')
    opr_perm = '+ - * /'
    
    try:
        n1_real = float(n1)
        n2_real = float(n2)
    except:
        print('Você não digitou números válidos.')
        continue
        
    
    if opr not in opr_perm:
        print('Operador inválido.')
        continue
        
    print('Realizando sua conta...')
    if opr == '+':
        print(f'SOMA: {n1_real + n2_real}')
    if opr == '-':
        print(f'SUBTRAÇÃO: {n1_real - n2_real}')
    if opr == '/':
        print(f'DIVISÃO: {n1_real/n2_real}')
    if opr == '*':
        print(f'MULTIPLICAÇÃO: {n1_real * n2_real}')

    resp = input('Deseja continuar [S/N]: ')
    if resp == 'N' or resp == 'n':
        break

print(f'{server} saiu')



# sempre começar com os possíveis erros de dados.