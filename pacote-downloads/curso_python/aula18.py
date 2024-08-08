nome = 'Stephany'
print('pha' in nome)
print('o' in nome)
print('tep' not in nome)
print('zero' not in nome)
print(10 * '-')
teste = input('Digite uma palavra: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in teste:
    print(f'{encontrar} está em {teste}')
else:
    print(f'{encontrar} não está em {teste}')
    