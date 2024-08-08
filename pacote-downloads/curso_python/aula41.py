lista = ['D', 'F', 'J', 'K']
lista_enumerada = enumerate(lista)  # o enumerate enumera os ítens de uma lista

for indice in lista_enumerada:
    print(indice)
    
print('OUTRA FORMA ------')
vet = [1, 2 ,3]

for item in enumerate(vet):
    indices, nome = item
    print(indices, nome)

print('OUTRA FORMA ---------')

vetor = ['ste', 'nat', 'Jack', 'Gab']
for i, nomes in enumerate(vetor):
    print(i, nomes)
