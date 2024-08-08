"""
Função lambda em py
são funções anônimas que contém apenas uma linha;
tudo deve ser contido dentro de uma única expressão;

"""
#lista = [1,56,2,78,56,4,436,7,8,1,24]
#lista.sort() #lista.sort(reverse = True) : de trás para frente
# print(lista)

lista = [
    {'nome':'Stephany','sobrenome':'Resque'},
    {'nome':'Nathália','sobrenome':'Moreno'},
    {'nome':'Marcus','sobrenome':'Vinícius'}
         ]

#def ordena(item):
#    return item['nome']

#lista.sort(key=ordena)

#for item in lista:
#    print(item)


lista.sort(key=lambda item : item['nome'])

for item in lista:
    print(item)

print()

def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista,key=lambda item : item['nome']) #sorted retorna uma cópia rasa da lista já feita;
l2 = sorted(lista,key=lambda item : item['sobrenome'])

exibir(l1)
exibir(l2)





