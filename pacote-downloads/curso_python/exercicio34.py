
num = int(input('Informe um número inteiro: '))
unidade = int(input('[1] para Binário\n[2] para Octal\n[3] para Hexadecimal\nSelecione: '))

if unidade == 1:
    print(f'VALOR EM BINÁRIO: {bin(num)[2:]}')
elif unidade == 2:
    print(f'VALOR EM OCTAL: {oct(num)[2:]}')
elif unidade == 3:
    print(f'VALOR EM HEXADECIMAL: {hex(num)[2:]}')
else:
    print('Valor inválido.')


