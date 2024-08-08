lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']

def zipper(l1, l2):
    intervalo = min(len(l1), len(l2))
    return [
        (lista1[i],lista2[i]) for i in range(intervalo)
    ]
        

zipado = zipper(lista1, lista2)
print(zipado)

#entretanto existe uma função que já faz isso
