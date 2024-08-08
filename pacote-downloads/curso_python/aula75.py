'''
Filtro em list c.;
'''

produtos = [
    {'nome':'p1','preco':10},
    {'nome':'p2','preco':12},
    {'nome':'p3','preco':14}
]

#lista = [n for n in range(10) if n > 5]
#print(lista)

novos_produtos = [
    {**produto, 'preco':produto['preco']*1.05}
    if produto['preco'] > 12 else {**produto}
    for produto in produtos 
    if produto['preco'] > 10
]

print(*novos_produtos, sep='\n')