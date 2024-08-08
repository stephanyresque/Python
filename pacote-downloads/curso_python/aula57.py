"""

Dicionários em Python (dict)
Dicionários são estruturas de dados do tipo par de "chave" e "valor"
Chaves podem ser consideradas como "índices" que vimos nas listas e podem ser de tipos imutáveis (str, int, float, bool, tuple)
O valor pode ser de qualquer tipo, incluindo outro dicionário
Usamos as chaves "{}" ou a classe dict para criar um dicionário
listas e dict são mutáveis

"""

pessoa = {
    'nome':'Stephany',
    'sobrenome':'Resque',
    'idade': 20,
    'altura': 1.64,
    'endereços': [
        {'rua': 'tal tal', 'numero': 45},
        {'rua': 'la la', 'numero': 27},
    ]
}
print(pessoa['nome'])
print(pessoa['sobrenome'])

for chave in pessoa:
    print(chave, pessoa[chave])


