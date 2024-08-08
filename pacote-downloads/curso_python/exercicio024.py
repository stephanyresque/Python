nome = str(input('Informe seu nome completo: '))

print(f'Seu primeiro nome é {nome[0:nome.find(' ')]}')
print(f'Seu último nome é{nome[nome.rfind(' '):]}')

nome2 = str(input('Outro nome: '))
lista = nome2.split()

print(f'O primeiro nome é {lista[0]}')
print(f'O último nome é {lista[-1]}')

