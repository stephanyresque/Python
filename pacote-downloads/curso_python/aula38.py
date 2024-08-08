lista = [10, 20 , 30, 40]
del lista[2]
print(lista)
print(lista[2])

lista1 = [1, 2, 3 , 4]
nome = lista1.pop()
lista1.append(7)
print(lista1)

lista2 = [1, 2, 3]
lista2.insert(0, 0)
print(lista2)

"""
append - adiciona um íntem ao final da lista
insert - adiciona um íntem na posição escolhida
pop - remove o último ítem (a não ser que você especifique)
del - remove tbm, mas você deve especificar a posição
clear - limpa a lista
extend - estende a lista
+ - concatenta a lista

"""
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)

vet = ['Stephany', 'ama', 'a Nathália']
for item in vet:
    print(item)
    