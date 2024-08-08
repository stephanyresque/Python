princes = 'Nathália'
i = 0
while i < len(princes):
    letra = princes[i]
    print(letra)
    if letra == 'h':
        break

    i = i + 1
else:
    print('O else entra aqui')

print('Mas aqui não')
