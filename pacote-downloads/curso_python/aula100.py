lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

def soma(l1, l2):
    intervalo = min(len(l1), len(l2))
    return [
        (lista_a[i] + lista_b[i]) for i in range(intervalo)
    ]

soma_lista = soma(lista_a, lista_b)
print(soma_lista)

soma_facil = [x + y for x, y in zip(lista_a, lista_b)]
print(soma_facil)