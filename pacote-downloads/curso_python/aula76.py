#lista = []

#for x in range (3):
#    for y in range(3):
#        lista.append((x,y))

lista = [
    (x, y)
    for x in range(1, 4)
    for y in range(1, 4)
]

print(lista)
