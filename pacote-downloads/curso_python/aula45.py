# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Nathália', 'Ste', 1, 2, 3, 4, 'Moreno']
tupla = 'Python', 'as vezes', 'me cansa.'

p, s, *_, u = lista
print(p, u)

for item in lista:
    print(item, end=' ')

print(' ')

print(*lista)
print(*string)
print(*tupla)

