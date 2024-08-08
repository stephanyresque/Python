primeiro_termo = int(input('Informe o 1° termo: '))
razao = int(input('Informe a razão: '))

for i in range(10):
    print(f'{primeiro_termo+(razao*i)}', end=' -> ')
print('ACABOU')


