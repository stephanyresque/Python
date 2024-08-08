# reduce - faz a redução de um iterável em um valor
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def funcao_reduce(acumulador, produto):
    print('acumulador ', acumulador)
    print('produto ', produto)
    print()
    return acumulador + produto['preco']


total = 0
for p in produtos:
    total += p['preco']

total1 = (sum(p['preco'] for p in produtos))

total2 = reduce(
    funcao_reduce,
    produtos,
    0 #valor inicial -> acumulador 
)

total3 = reduce(
    lambda ac, p: ac+p['preco'],
    produtos,
    0
)

#print(total)
#print(total1)
#print(total2)
print()
print(total3)