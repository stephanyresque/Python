import random

lista = []
for i in range(1, 5):
    nome = input(f'ALUNO {i}: ')
    lista.append(nome)

random.shuffle(lista)

print(f'A orde de apresentação será: {lista}')



