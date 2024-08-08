"""
Mapeamento de dados com list c.;

"""
produtos = [
    {'nome':'p1','preco':10},
    {'nome':'p2','preco':12},
    {'nome':'p3','preco':14}
]
novos_produtos = [
    {**produto, 'preco':produto['preco']*1.05}
    if produto['preco'] > 12 else {**produto}
    for produto in produtos
]
print(novos_produtos)
print()
print(*novos_produtos, sep='\n')

