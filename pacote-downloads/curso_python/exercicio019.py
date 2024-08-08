nome = str(input('Digite seu nome: ')).strip() #tira os espaços antes e depois

print(f'Seu nome maiúsculo: {nome.upper()}')
print(f'Seu nome minúsculo: {nome.lower()}')
print(f'Seu nome tem {len(nome)-nome.count(' ')} letras')
#print(f'Seu primeiro nome tem {nome.find(' ')} letras')

nomes = nome.split() # coloca dentro de uma lista
print(f'Seu primeiro nome é {nomes[0]} e tem {len(nomes[0])} letras.')




