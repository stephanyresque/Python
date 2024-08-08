"""
combinations, permutations e product - itertools;
combinação - ordem não importa - iterável + tamanho do grupo;
permutação - ordem importa;
produto - ordem importa e repete valores únicos;

"""
from itertools import combinations, permutations, product

def motra_inter(iterador):
    print(*list(iterador), sep='\n')
    print()

pessoas = [
    'João', 'Maria', 'José', 'Taldo'
]

camisetas = [
    ['branca', 'preta'],
    ['p', 'm'],
    ['fem', 'masc', 'unisex'],
]

#motra_inter(combinations(pessoas, 2))
#motra_inter(permutations(pessoas, 2))
motra_inter(product(*camisetas))
