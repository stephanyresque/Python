n = input('Quantos números que realocar: ')
n = int(n)

lista = []

for i in range(1, n+1):
    numero = int(input(f'Digite o {i}° valor: '))
    lista.append(numero)

lista.sort()

print(f'Menor número: {lista[0]}')
print(f'Maior número: {lista[-1]}')





