numero = input('Qual número você gostaria de dobrar: ')

try:
    print(f'STR: {numero}')
    numero_float = float(numero)
    print(f'FLOAT: {numero_float}')
    print(f'O dobro de {numero} é {numero_float * 2}')
        
except:
    print('Isso não é um número.')


