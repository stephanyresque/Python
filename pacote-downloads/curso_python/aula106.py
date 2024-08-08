# filter é um filtro funcional

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

def mudar_preco(produto):
    return produto['preco'] > 20

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = [
    p for p in produtos
    if p['preco'] > 20
]

novos_produtos_2 = filter(
    lambda p: p['preco'] > 20,
    produtos
)

novos_produtos_3 = filter(
    mudar_preco,
    produtos
)

print_iter(produtos)
print_iter(novos_produtos)
print_iter(novos_produtos_2)
print_iter(novos_produtos_3)

