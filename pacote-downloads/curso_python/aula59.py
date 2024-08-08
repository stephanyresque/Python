"""
MÉTODOS NAS CHAVES
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - apaga um item com a chave especificada (del)
popitem - apaga o último item adicionado
update - atualiza um dicionário com outro

"""
pessoa = {
    'nome':'Stephany',
    'sobrenome':'Resque',
}

print(len(pessoa))
print(list(pessoa.keys()))
print(list(pessoa.values()))

for valor in pessoa.values():
  print(valor)

print(list(pessoa.items()))

for chave, item in pessoa.items():
    print(chave, item)

pessoa.setdefault('idade', 20)
print(pessoa['idade'])
