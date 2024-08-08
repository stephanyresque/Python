"""
list comprehesion
uma forma rápida de criar listas a partir de iteráveis;

"""

lista = []
#for numero in range(11):
#    lista.append(numero)

lista = [numero for numero in range(11)]

print(lista)
print()

lista = [
    numero * 2   
    for numero in range(11)
    ]
print(lista)
