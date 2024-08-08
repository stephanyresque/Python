
pessoa = {
    'nome':'Stephany',
    'sobrenome':'Resque'
}

a, b = pessoa
print(a, b)
a, b = pessoa.values()
print(a, b)
a, b = pessoa.items()
print(a, b)

(a1, a2),(b1, b2) = pessoa.items()
print(a1, a2)
print(b1, b2)

for chave, valor in pessoa.items():
    print(chave, valor)
    