lista = []
for i in range(2):
    n = int(input())
    lista.append(n)

lista.sort()

if(lista[0] == lista[1]):
    print('Os valores são iguais')
else:
    print(f'Maior valor: {lista[1]}')
    print(f'Menor valor: {lista[0]}')


