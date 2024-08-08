
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = [
    {**produto, 'preco':round(produto['preco']*1.1, 2)}
    for produto in produtos
]
print(*novos_produtos, sep='\n')
print()

produtos.sort(key=lambda item : item['nome'], reverse=True)


produtos_ordenados_por_nome = produtos

print(*produtos_ordenados_por_nome, sep='\n')
print()

produtos.sort(key=lambda item : item['preco'])
produtos_ordenados_por_preco = produtos

print(*produtos_ordenados_por_preco, sep='\n')
