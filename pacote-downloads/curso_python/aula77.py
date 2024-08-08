"""
Dictionary comprehension e Set comprehension;

"""

produto = {
    'nome':'caneta azul',
    'preco':2.50,
    'categoria':'escritório',
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor  
    for chave, valor in produto.items()
    if chave != 'categoria'
}

print(dc)
print()

l1 = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),

]

db = {
    chave: valor 
    for chave, valor in l1
}
print(db)