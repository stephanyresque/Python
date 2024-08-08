n1 = input('Digite o 1º valor: ')
n2 = input('Digite o 2º valor: ')
primeiro_valor = int(n1)
segundo_valor = int(n2)

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} é maior.')
elif primeiro_valor == segundo_valor:
    print('Os valores são iguais.')
else:
    print(f'{segundo_valor=} é maior.')
