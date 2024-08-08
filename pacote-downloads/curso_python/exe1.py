n1 = input('Digite um número inteiro: ')

if n1 and (n1.isdigit()):
    numero_int = int(n1)
    if (numero_int % 2 == 0):
        print(f'O número {numero_int} é par.')
    else:
        print(f'O número {numero_int} é ímpar.')
else:
    print('Você não informou um número inteiro')

