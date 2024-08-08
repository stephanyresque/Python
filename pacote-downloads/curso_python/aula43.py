"""
split = divide uma string (retorna uma lista)
join = une uma str
strip = tira os espaços inicial e final

"""
frase = '     Ohe só que    , coisa legal      '
lista_crua = frase.split(',')

lista = []
for i, frase in enumerate(lista_crua):
    lista.append(lista_crua[i].strip())

print(lista_crua)
print(lista)

frase_unida = '-'.join(lista)
print(frase_unida)
