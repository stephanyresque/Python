from dados import produtos
import copy

novos_produtos = [
    {**p, 'preco':round(p['preco']*1.1, 2)}
    for p in copy.deepcopy(produtos)
    
]
print(*novos_produtos, sep='\n')
print()

produtos_ordenados_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p:p['nome'],
    reverse=True
)

print(*produtos_ordenados_nome, sep='\n')
print()

produtos_ordenados_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p:p['preco']
)

print(*produtos_ordenados_preco, sep='\n')



